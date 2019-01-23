from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps

app = Flask(__name__)
api = Api(app)

class Welcome(Resource):
    def get(self):
        result = {'data': 'welcome'}
        return jsonify(result)
        
class Test(Resource):
    def get(self):
        result = {'data': 'test'}
        return jsonify(result)

api.add_resource(Welcome, '/')
api.add_resource(Test, '/test')


if __name__ == '__main__':
     app.run()
