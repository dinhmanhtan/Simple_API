from models import (Employee, db)
from flask import request
from flask_restful import Resource


class EmployeeList(Resource):

    # GET employee
    # @app.get("/api/employees")
    def get(self):

        employees = Employee.query.all()
        result = []

        for emp in employees:
            employee = {"id":emp.id, "name":emp.name, "age":emp.age, "description":emp.description}
            result.append(employee)

        return {"code":200, "message":"success", "data":result}, 200

    # CREATE employee
    # @app.post("/api/employees")
    def post(self):
        
        data = request.get_json()

        for arg in ("name", "age", "description"):
            if arg not in data:
                return {"code":400, "message":"missing arguments"}, 400

        name = data["name"]
        age = data["age"]
        descripton = data["description"]

        try:
            employee = Employee(name=name,age=age,description=descripton)
            db.session.add(employee)
            db.session.commit()
        except:
            return {"code":500,"error":"internal server error"}, 500

        data_employee = {"name":employee.name, "age": employee.age, "description": employee.description}

        return {"code":201,"message":"success", "data": data_employee}, 201


class EmployeesDetail(Resource):

    # GET all employees
    # @app.get("/api/employees/<int:employee_id>")
    def get(self, employee_id):

        employee = Employee.query.filter_by(id=employee_id).first()

        if(employee == None):
            return {"code":404, "message": "employee doesn't exist"}

        id = employee.id
        name = employee.name
        age = employee.age
        description = employee.description
        data = {"id":id, "name":name, "age":age, "description":description}

        return {"code":200, "message":"success", "data":data}, 200

    # UPDATE employee
    # @app.patch("/api/employees/<int:employee_id>")
    def patch(self, employee_id):
        data = request.get_json()
        employee = Employee.query.filter_by(id=employee_id).first_or_404()

        for attr,value in data.items():
            setattr(employee,attr,value)

        db.session.commit()
        employee = Employee.query.filter_by(id=employee_id).first_or_404()
        data = {"name":employee.name, "age": employee.age, "description": employee.description}

        return {"code":200, "message":"success","data":data}, 200

    
    # DELETE employee
    # @app.delete("/api/employees/<int:employee_id>")
    def delete(self, employee_id):
        Employee.query.filter_by(id=employee_id).delete()

        db.session.commit()
        return {"code":204, "message":"success"}, 204
    