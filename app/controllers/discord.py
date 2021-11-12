from flask_restful import Resource
from flask import request, jsonify
import json
import requests


class DiscordPullRequest(Resource):
    def post(self):
        d = json.loads(request.data)
        r = requests.post(
            "https://discord.com/api/webhooks/908349291960102993/bP7nitOCJEifc4O_peDGHlyrbPApyVgf60NOLj2N_180lKpCBnBTTPjjjGERjJAYoNIf",
            json={
                "username": "Azure Git Bot - TCL Noti",
                "avatar_url": "https://swimburger.net/media/0zcpmk1b/azure.jpg",
                "content": "Text message. Up to 2000 characters.",
                "embeds": [
                    {
                        "author": {
                            "name": d["resource"]["createdBy"]["displayName"],
                            "url": d["resource"]["createdBy"]["url"],
                            "icon_url": d["resource"]["createdBy"]["imageUrl"],
                        },
                        "title": "Pull Request",
                        "url": d["resource"]["url"],
                        "description": d["detailedMessage"]["markdown"],
                        "color": 15258703,
                    }
                ],
            }
        )


class DiscordDeployCompleted(Resource):
    def post(self):
        return {"data": request.data}
