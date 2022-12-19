import os
from flask import Flask
from . import fileUpload
from . import memory
from . import login

from flask_cors import CORS, cross_origin #pip install flask_cors
#flask run --host=0.0.0.0

def create_app(test_config=None):	
    app = Flask(__name__, instance_relative_config=True) # creates the flask instance
    #CORS처리하기 - 외부로부터 접근 허용 되도록 해야 한다 
    CORS(app) 

    app.config.from_mapping(SECRET_KEY='werljesaf')
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #http://127.0.0.1:5000/
    
    app.register_blueprint(fileUpload.app)
    app.register_blueprint(login.app)
    app.register_blueprint(memory.app)
    
    return app
