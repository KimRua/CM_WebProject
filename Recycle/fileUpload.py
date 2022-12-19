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

# def load_model(file_name="gabage_model.h5"):
#     model_load = keras.models.load_model(file_name)
#     return model_load

app = Blueprint('fileUpload', __name__)
api = Api(app) 

db = DBMoudel.Database()

# UPLOAD_PATH=r"..\myproject\project2\upload"
UPLOAD_PATH=r"../web/Main_CM_Html/uploads/img/"

class FileUpload(Resource):
    def post(self):
        file = request.files["image"]
        if file:
            filename = file.filename
            sfilename = os.path.join(UPLOAD_PATH, filename)
            file.save(sfilename)
            
            # img = Image.open(r'../myproject/project2/upload/' + filename)
            # img_resize = img.resize((512, 384))
            # img_resize.save(r'../myproject/project2/upload/' + filename)
            
            # model = load_model(r"..\myproject\project2\gabage_model.h5")
            # test_img = load_img(sfilename) # word = {'cardboard' : 0, 'glass' : 1, 'metal' : 2, 'paper' : 3, 'plastic' : 4, "trash" : 5}
            # arr_img = img_to_array(test_img)
            # img = arr_img.reshape((1,)+arr_img.shape)
            # predict = model.predict(img)
            # result = predict.argmax()
        # return str(result)
        return str(random.randint(0, 5))

api.add_resource(FileUpload, '/image/upload')