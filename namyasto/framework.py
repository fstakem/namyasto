# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    8.10.16   
#
# -----------------------------------------------------------------------------------------------


# Libraries
import json
import os
import sys
import logging

from flask import Flask

from namyasto import app_path
from namyasto.api.version_1_0_0 import app_v1_0_0


# Framework globals
# -----------------------------------------------------
flask_app = None
current_app = app_v1_0_0


# Helper functions
# -----------------------------------------------------
def read_config(config_path):
    with open(config_path) as data_file:
        data = json.load(data_file)

    return data

def load_config(env):
    try:
        config_path = os.path.join(app_path, 'config', env + '.json')
        config = read_config(config_path)
    except FileNotFoundError as e:
        # TODO - handle
        sys.exit(-1)

    return config

def setup_logger(config):
    # TODO - create app logger
    logger = None
    werkzeug_logger = logging.getLogger('werkzeug')
    werkzeug_logger.setLevel(logging.ERROR)

    return logger

def create_flask_app(config):
    flask_app = Flask(__name__)
    flask_app.secret_key                                = 'TTS96tKYthZh2V2jO7Bwi1c4BO0BFYfe8YnDegkg'

    return flask_app

def register_versions(flask_app):
    flask_app.register_blueprint(app_v1_0_0, url_prefix='/v1_0_0')
    #flask_app.register_blueprint(current_app)
    current_app

