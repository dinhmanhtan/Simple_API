import os

class Config(object):
    

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:tan@localhost/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ITEM_METHODS = ['GET', 'PATCH', 'DELETE', 'POST']