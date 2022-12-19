import cv2
from flask import Flask, request, Response, Blueprint
import json 
from flask_restful import Resource, Api, reqparse 
import os
from keras.utils import np_utils, img_to_array, load_img
import numpy as np
from keras.layers import *
from tensorflow import keras
from PIL import Image
import random
from . import DBMoudel

app = Blueprint('login', __name__)
api = Api(app) 

db = DBMoudel.Database()

parser = reqparse.RequestParser()
parser.add_argument("indexs")
parser.add_argument("ids")
parser.add_argument("passwords")
parser.add_argument("names")

class login(Resource):
    def get(self, ids=None):
        sql = """
        select indexs, ids, passwords, names
        from LoginsRecycle where ids=%s
        """
        loginData = db.executeOne(sql, (ids, ))

        jsonStr = json.dumps(loginData, ensure_ascii=False).encode('utf-8')
        return Response(jsonStr, content_type="application/json;charset=utf-8")

    def post(self):
        args = parser.parse_args() 
        sql = """
            insert into LoginsRecycle(ids, passwords, names)
            values(%s, %s, %s)
        """
        db.execute(sql, (args['ids'], args['passwords'], args['names']))
        return "success"

api.add_resource(login, '/recycle/login/view/<string:ids>',
                        '/recycle/login/insert')