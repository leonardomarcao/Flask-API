import logging
import os
from flask import Flask, jsonify, request
from app import main
from app.main.api import api

# Flask App Initialization
app = Flask(__name__)
app.config.from_object(main.settings[os.environ.get('APPLICATION_ENV', 'default')])

# Logs Initialization
console = logging.getLogger('console')

@app.route('/pr-azure', methods=['POST'])
def get_pr_from_azure():
    return jsonify({'pr_body': request.form})


# Flask API Initialization
api.init_app(app)
