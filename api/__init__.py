from flask_restful import Api
from api.employees import EmployeeList, EmployeesDetail

# Flask API Configuration
api = Api(
    catch_all_404s=True,
    prefix='/api'
)

api.add_resource(EmployeeList,'/employees')
api.add_resource(EmployeesDetail,'/employees/<int:employee_id>')