from flask_restful import Resource
from flask import request, jsonify


class DiscordPullRequest(Resource):    
    def post(self):
        return jsonify({
            "data": request.data
        })

class DiscordDeployCompleted(Resource):
    def post(self):
        return jsonify({
            "data": request.data
        })