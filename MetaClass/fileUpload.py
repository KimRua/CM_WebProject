from flask import request,Blueprint
from flask_restful import Resource, Api
import os
from . import object

app = Blueprint('fileUpload', __name__)
api = Api(app)

# db = DBMoudel.Database()

UPLOAD_PATH = './MetaClass/upload'
class FileUpload(Resource) :
    def post(self):
        file = request.files["image"]
        if file:
            filename = file.filename
            sfilename = os.path.join('./MetaClass/upload/', filename)
            file.save(sfilename)
        return object.GetAPIResult(filename)

api.add_resource(FileUpload, '/metaclass/image/upload')