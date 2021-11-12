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
                        "color": 52152219,
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
        d = json.loads(request.data)
        r = requests.post(
            "https://discord.com/api/webhooks/908688772428873748/mvpQNRcsuJ4mZHMaV7cc9zWuWHurJtdqkjnRg0P40oHteUkN2lkcNNyoGEG6GY5_Je1F",
            json={
                "username": "Azure CI Bot - TCL Notification",
                "avatar_url": "https://swimburger.net/media/0zcpmk1b/azure.jpg",
                "embeds": [
                    {
                        "fields": [
                            {
                                "name": "Requerido por",
                                "value": d["resource"]['requests'][0]['requestedFor']['displayName'],
                                "inline": True
                            },
                            {
                                "name": "Última Alteração",
                                "value": d["resource"]["lastChangedBy"]["displayName"],
                                "inline": True
                            },
                        ],
                        "title": d["message"]['text'],
                        "description": d["detailedMessage"]["markdown"],
                        "color": 3917496,
                        "footer": {
                          "text": "Build concluído com sucesso!",
                          "icon_url": "https://cdn-icons-png.flaticon.com/512/1721/1721539.png"
                        }
                    },
                ],
            }
        )

