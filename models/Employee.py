from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key = True)
    name = db. Column(db.String(100), nullable = False)
    age = db.Column(db.Integer(), nullable = False)
    description = db.Column(db.String(100), nullable = False)
    

    def __repr__(self):
        return "<Employee %r>" % self.name