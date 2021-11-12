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
                "username": "Azure Git Bot - TCL Notification",
                "avatar_url": "https://swimburger.net/media/0zcpmk1b/azure.jpg",
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
                        "footer": {
                          "text": "Por favor, faça revisão do PR, aprove e efetue o merge para prosseguir na pipeline de CI.",
                          "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Octicons-git-pull-request.svg/1200px-Octicons-git-pull-request.svg.png"
                        }
                    },
                ],
            }
        )


class DiscordDeployCompleted(Resource):
    def post(self):
        return {"data": request.data}
