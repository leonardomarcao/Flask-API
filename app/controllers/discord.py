from flask_restful import Resource
from flask import request


class DiscordPullRequest(Resource):    
    def post(self):
        return {
            "data": request.data
        }

class DiscordDeployCompleted(Resource):
    def post(self):
        return {
            "data": request.data
        }