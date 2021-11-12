from flask_restful import Resource
from flask import request, jsonify
import json
import requests


class DiscordGitNotification(Resource):
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
                        "color": 15258703,
                        "footer": {
                          "text": "Por favor, faça revisão do PR, aprove e efetue o merge para prosseguir na pipeline de CI.",
                          "icon_url": "https://images.emojiterra.com/google/android-pie/512px/2615.png"
                        }
                    },
                ],
            }
        )
        return {"status_code": r.status_code}


class DiscordCIReleaseCompleted(Resource):
    def post(self):
        d = json.loads(request.data)
        r = requests.post(
            "https://discord.com/api/webhooks/908704900609867856/iEb4MWtMo7RUBj4mu_gbXbABKkysbSlY_FW1alnqlLjZnA4u-bLMDBd9B-xX6OhzgOj6",
            json={
                "username": "Azure CI Bot - TCL Notification",
                "avatar_url": "https://swimburger.net/media/0zcpmk1b/azure.jpg",
                "embeds": [
                    {
                        "fields": [
                            {
                                "name": "Owner",
                                "value": d["resource"]['environment']['owner']['displayName'],
                            },
                            {
                                "name": "Name",
                                "value": d["resource"]['environment']['name'],
                                "inline": True
                            },
                            {
                                "name": "Status",
                                "value": d["resource"]['environment']['status'],
                                "inline": True
                            }
                        ],
                        "title": f"Release: {d['message']['text']} - {d['resource']['project']['name']}",
                        "url": d['resource']['environment']['release']['_links']['web']['href'],
                        "description": d["detailedMessage"]["markdown"],
                        "color": 3917496,
                        "footer": {
                          "text": "Release concluído!",
                          "icon_url": "https://static.thenounproject.com/png/1410037-200.png"
                        }
                    },
                ],
            }
        )
        return {"status_code": r.status_code}


class DiscordCIBuildCompleted(Resource):
    def post(self):
        d = json.loads(request.data)
        r = requests.post(
            "https://discord.com/api/webhooks/908704900609867856/iEb4MWtMo7RUBj4mu_gbXbABKkysbSlY_FW1alnqlLjZnA4u-bLMDBd9B-xX6OhzgOj6",
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
                            {
                                "name": "Definição",
                                "value": d["resource"]["definition"]["name"],
                                "inline": True
                            },
                            {
                                "name": "Status",
                                "value": d["resource"]["status"],
                                "inline": True
                            },
                        ],
                        "title": f"Build: {d['message']['text']}",
                        "description": d["detailedMessage"]["markdown"],
                        "color": 3917496,
                        "footer": {
                          "text": "Build concluído!",
                          "icon_url": "https://static.thenounproject.com/png/1909170-200.png"
                        }
                    },
                ],
            }
        )
        return {"status_code": r.status_code}
