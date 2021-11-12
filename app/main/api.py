from flask_restful import Api
from app.controllers.discord import DiscordGitNotification, DiscordCINotification
from app.main.errors import errors

# Flask API Configuration
api = Api(catch_all_404s=True, errors=errors, prefix="/api")

api.add_resource(DiscordGitNotification, "/discord_git_notification")
api.add_resource(DiscordCINotification, "/discord_ci_notification")
