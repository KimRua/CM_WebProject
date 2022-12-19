# from flask import Response, Blueprint
# from flask_restful import Resource, Api,reqparse
# import json
# from database import Database

# app = Blueprint('object', __name__)
# api = Api(app)

# parser = reqparse.RequestParser()
# parser.add_argument("indexs")
# parser.add_argument("ids")
# parser.add_argument("passwords")
# parser.add_argument("names")

# app = Blueprint('login', __name__)
# api = Api(app)

# class login(Resource): #Resource 클래스 상속받기 
#     def get(self, ids=None):
#         sql = """
#         select indexs, ids, passwords, names
#         from logins where ids=%s
#         """
#         loginData = Database.executeOne(sql, (ids, ))

#         jsonStr = json.dumps(loginData, ensure_ascii=False).encode('utf-8')
#         return Response(jsonStr, content_type="application/json;charset=utf-8")

#     def post(self):
#         args = parser.parse_args() 
#         sql = """
#             insert into logins(ids, passwords, names)
#             values(%s, %s, %s)
#         """
#         Database.execute(sql, (args['ids'], args['passwords'], args['names']))
#         return "success"


# api.add_resource(login, '/metaclass/login/view/<string:ids>',
#                         '/metaclass/login/insert')