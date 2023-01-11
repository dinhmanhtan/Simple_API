import psycopg2
import psycopg2.extras
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

conn = None

GET_USER = """SELECT * FROM users WHERE id = (%s)"""
GET_ALL_USERS = "SELECT * FROM users"

INSERT_USER = 'INSERT INTO users (name_,age,dob) VALUES (%s,%s,%s) RETURNING id'

try : 
    conn = psycopg2.connect(
    database="test", user='postgres', password='tan', host='127.0.0.1', port= '5432'
)
    with conn.cursor() as cur:

        CREATE_USER_TABLE = (
        "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY , name_ TEXT not null, age int, DoB TIMESTAMP);"
        )

        cur.execute(CREATE_USER_TABLE)

        #cur.execute(INSERT_USER,insert_value)
     
        # conn.commit()

except NameError:
    print(NameError)

@app.get("/api/users/<int:user_id>")
def get_user(user_id):
    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(GET_USER,(str(user_id)))

            result = cursor.fetchone()
            if(result == None ):
                return {"success":False}
            id = result["id"]
            name = result["name_"]
            age = result["age"]
            dob = result["dob"]


    return {"id":id,"name":name,"age":age,"DoB":dob},200

@app.get("/api/users")
def get_all_users():
    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(GET_ALL_USERS)
            
            result = []
            for user in cursor.fetchall():
                id = user["id"]
                name = user["name_"]
                age = user["age"]
                dob = user["dob"]
                u = {"id":id,"name":name,"age":age,"DoB":dob}
                result.append(u)

    return result,200

@app.post("/api/user")
def create_user():
    
    data = request.get_json()
    print(data)
    name = data["name"]
    age = data["age"]
    try:
        dob = datetime.strptime(data["dob"], "%m-%d-%Y %H:%M:%S")
    except KeyError:
        dob = datetime.utcnow()
    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(INSERT_USER,(name,age,dob))
            user_id = cursor.fetchone()["id"]
    return {"id":user_id,"message":f"User {name} created"},201

@app.patch("/api/user/<int:user_id>")
def update_user(user_id):
    data = request.get_json()




if __name__ == '__main__':
    app.run(debug=True)

