from flask import Flask, Blueprint
""" flask is our framework"""
""" Flask is the python class type"""
""" creating instances of our web app"""
""" blueprint defines a collection of views, templates, and static files that can be applied to an application"""


from .api.v1 import version1 as v1
from .api.v2 import version2 as v2
from flask_jwt_extended import JWTManager

def create_app():
    
    app = Flask(__name__)
    app.register_blueprint(v1)
    app.register_blueprint(v2)
    app.config['JWT_SECRET_KEY'] = 'wsedrftgrdesdrftgfrdeftgtfrdtfg'
    JWTManager(app)

    return app
