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
                            "icon_url": "https://cdn-icons-png.flaticon.com/512/1/1247.png",
                        },
                        "fields": [
                            {
                                "name": "Source",
                                "value": d["resource"]['sourceRefName'],
                                "inline": True
                            },
                            {
                                "name": "Target",
                                "value": d["resource"]['targetRefName'],
                                "inline": True
                            },
                        ],
                        "title": d["resource"]['title'],
                        "url": d["resource"]["_links"]['web']['href'],
                        "description": d["detailedMessage"]["markdown"],
                        "color": 15258703,
                        "footer": {
                          "text": "Por favor, faça revisão do PR, aprove e efetue o merge para prosseguir na pipeline de CI.",
                          "icon_url": "https://images.emojiterra.com/google/android-pie/512px/2615.png"
                        }
                    },
                ],
            }
        )


class DiscordDeployCompleted(Resource):
    def post(self):
        return {"data": request.data}
