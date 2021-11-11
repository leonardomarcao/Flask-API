from flask_restful import Resource
from flask import request, jsonify


class DiscordPullRequest(Resource):    
    def post(self):
        return {
            "data": jsonify(request.data)
        }

class DiscordDeployCompleted(Resource):
    def post(self):
        return {
            "data": jsonify(request.data)
        }