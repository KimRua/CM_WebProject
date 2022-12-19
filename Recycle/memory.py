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

app = Blueprint('memory', __name__)
api = Api(app)

db = DBMoudel.Database()

parser = reqparse.RequestParser()
parser.add_argument("indexs")
parser.add_argument("ids")
parser.add_argument("counts")
parser.add_argument("cardboard")
parser.add_argument("glass")
parser.add_argument("metal")
parser.add_argument("paper")
parser.add_argument("plastic")
parser.add_argument("trash")

class memory(Resource):
    def get(self, ids=None):
        sql = """
            select indexs, ids, counts, cardboard, glass, metal, paper, plastic, trash
            from MemoryRecycle where ids=%s
        """
        memoryData = db.executeOne(sql, (ids, ))

        jsonStr = json.dumps(memoryData, ensure_ascii=False).encode('utf-8')
        return Response(jsonStr, content_type="application/json;charset=utf-8")

    def post(self):
        args = parser.parse_args() 
        sql = """
            insert into MemoryRecycle(ids, counts, cardboard, glass, metal, paper, plastic, trash)
            values(%s, %s, %s, %s, %s, %s, %s, %s)
        """
        db.execute(sql, (args['ids'], args['counts'], args['cardboard'], args['glass'], args['metal'], args['paper'], args['plastic'], args['trash']))
        return "success"

    def put(self, ids=None):
        args = parser.parse_args() 
        sql = """
            update MemoryRecycle set counts=%s, cardboard=%s, glass=%s, metal=%s, paper=%s, plastic=%s, trash=%s
            where ids=%s
        """
        db.execute(sql, (args['counts'], args['cardboard'], args['glass'], args['metal'], args['paper'], args['plastic'], args['trash'], args['ids']))
        return "success"

api.add_resource(memory, '/recycle/memory/view/<string:ids>',
                        '/recycle/memory/insert',
                        '/recycle/memory/update')