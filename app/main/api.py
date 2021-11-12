from flask_restful import Api
from app.controllers.discord import DiscordGitNotification, DiscordCIBuildCompleted, DiscordCIReleaseCompleted
from app.main.errors import errors

# Flask API Configuration
api = Api(catch_all_404s=True, errors=errors, prefix="/api")

api.add_resource(DiscordGitNotification, "/discord_git_notification")
api.add_resource(DiscordCIReleaseCompleted, "/discord_ci_release_notification")
api.add_resource(DiscordCIBuildCompleted, "/discord_ci_build_notification")
