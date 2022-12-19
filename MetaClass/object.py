from flask import Response, Blueprint
from flask_restful import Resource, Api, reqparse
# from matplotlib.font_manager import json_load
import urllib3
import json
import base64
import matplotlib.pyplot as plt
from PIL import Image
import os
from . import database

app = Blueprint('object', __name__)
api = Api(app)

db = database.Database()

openApiURL = "http://aiopen.etri.re.kr:8000/ObjectDetect"
accessKey = "ad9e100b-de95-4b7e-8b69-5931f47cb4a3"
type = "jpg"

class ObjectList(Resource):
    def get(self):
        return GetAPIResult()


class Object(Resource):
    def get(self):
        json_List = GetAPIResult()
        count = 0
        for object in json_List:
            if object.get('class') == "chair":
                count += 1
        return count

class GetObjectCount(Resource):
    def get(self):
        with open("./MetaClass/count.txt", "r") as f:
            result = int(f.read())
        return result
    
def GetAPIResult(filename):
    imageFilePath = "./MetaClass/upload/"

    # 이미지 크기 조정
    img = Image.open(imageFilePath + filename)
    imgResize = img.resize((int(img.width / 3), int(img.height / 3)))
    imgResize.save(imageFilePath + "r" +  filename)

    file = open(imageFilePath + "r" + filename, "rb")
    imageContents = base64.b64encode(file.read()).decode("utf8")
    file.close()
    
    requestJson = {
        "access_key": accessKey,
        "argument": {
            "type": type,
            "file": imageContents
        }
    }
    
    http = urllib3.PoolManager()
    response = http.request(
        "POST",
        openApiURL,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        body=json.dumps(requestJson)
    )

    # 이미지 지우기
    os.remove(imageFilePath + filename)
    os.remove(imageFilePath + "r" + filename)

    json_string = str(response.data)[2:-1:]
    #ShowGraph(json_string)
    json_object = json.loads(json_string).get('return_object')
    try:
        json_List = json_object['data']
    except:
        return "분석 실패. 다시 촬영해주세요."


    # 수정된 부분
    count = 0
    for object in json_List:
        if object.get('class') == "person":
            count += 1
    with open("./MetaClass/count.txt", "w") as f:
            f.write(str(count))
    return count


    # return json_List

# def ShowGraph(json_string):
#     json_object = json.loads(json_string).get('return_object')
#     json_Array = json_object['data']

#     fig = plt.figure()
#     ax = fig.add_subplot(111)
#     ax.axis((0,2000, 1160, 0))
#     ax.set_aspect('equal', adjustable='box')
    
#     for object in json_Array:
#         if object.get('class') == "person":
#             print(object.get('x'), object.get('y'))
#             plt.scatter(int(object.get('x')), int(object.get('y')))
    
#     plt.show()

api.add_resource(ObjectList, '/metaclass/object/list')
api.add_resource(Object, '/metaclass/object')

api.add_resource(GetObjectCount, '/metaclass/getobjectcount')