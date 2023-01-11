from flask import Flask,  request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

class Config(object):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:tan@localhost/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ITEM_METHODS = ['GET', 'PATCH', 'DELETE', 'POST']


app.config.from_object(Config)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:tan@localhost/test'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['ITEM_METHODS'] = ['GET', 'PATCH', 'DELETE', 'POST']

db = SQLAlchemy(app)

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key = True)
    name = db. Column(db.String(100), nullable = False)
    age = db.Column(db.Integer(), nullable = False)
    description = db.Column(db.String(100), nullable = False)


    def __repr__(self):
        return "<Employee %r>" % self.name

# GET employee
@app.get("/api/employees/<int:employee_id>")
def get_user(employee_id):

    employee = Employee.query.filter_by(id=employee_id).first_or_404()

    if(employee == None ):
        return {"success":False}
    id = employee.id
    name = employee.name
    age = employee.age
    description = employee.description

    return {"id":id,"name":name,"age":age,"description":description},200

# GET all employees
@app.get("/api/employees")
def get_all_users():
    employees = Employee.query.all()
    result = []
    for emp in employees:
        employee = {"id":emp.id,"name":emp.name,"age":emp.age,"description":emp.description}
        result.append(employee)
    return result

# CREATE employee
@app.post("/api/employee")
def create_user():
    
    data = request.get_json()
    name = data["name"]
    age = data["age"]
    descripton = data["description"]
    try:
        employee = Employee(name=name,age=age,description=descripton)
        db.session.add(employee)
        db.session.commit()
    except:
        return {"success":False}

    return {"success":True,"message":f"employee {name} created"},201

# UPDATE employee
@app.patch("/api/employees/<int:employee_id>")
def update_employee(employee_id):
    data = request.get_json()
    employee = Employee.query.filter_by(id=employee_id).first_or_404()
    for attr,value in data.items():
        setattr(employee,attr,value)
    db.session.commit()
    return {"success":True}


# DELETE employee
@app.delete("/api/employees/<int:employee_id>")
def delete_employee(employee_id):
    Employee.query.filter_by(id=employee_id).delete()

    db.session.commit()
    return {"success": True},204

with app.app_context():
    db.create_all()
if __name__ == '__main__':
    app.run(debug=True)
