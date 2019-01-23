from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps

app = Flask(__name__)
api = Api(app)

class Welcome(Resource):
    def get(self):
        result = {'data': 'true'}
        return jsonify(result)
        

api.add_resource(Welcome, '/welcome') # Route_2


if __name__ == '__main__':
     app.run()
