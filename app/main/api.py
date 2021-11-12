from flask_restful import Api
from app.controllers.discord import DiscordBuildCompleted, DiscordPullRequest, DiscordReleaseCompleted
from app.main.errors import errors

# Flask API Configuration
api = Api(catch_all_404s=True, errors=errors, prefix="/api")

api.add_resource(DiscordPullRequest, "/discord_pr_notification")
api.add_resource(DiscordBuildCompleted, "/discord_build_notification")
api.add_resource(DiscordReleaseCompleted, "/discord_release_notification")
