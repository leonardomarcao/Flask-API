from flask_restful import Api
from app.controllers.discord import DiscordDeployCompleted, DiscordPullRequest
from app.main.errors import errors

# Flask API Configuration
api = Api(catch_all_404s=True, errors=errors, prefix="/api")

api.add_resource(DiscordPullRequest, "/discord_pr_notification")
api.add_resource(DiscordDeployCompleted, "/discord_deploy_notification")
