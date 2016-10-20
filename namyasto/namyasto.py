# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    8.10.16   
#
# -----------------------------------------------------------------------------------------------


# Libraries
import os
import time
from datetime import datetime
import random

from flask import request, url_for, jsonify

from namyasto import app_path
from namyasto.framework import load_config, setup_logger, create_flask_app
from namyasto.framework import register_versions



# Config
flask_env   = os.environ['ENV'].lower()
config      = load_config(flask_env)
logger      = setup_logger(config)
flask_app   = create_flask_app(config)
_           = register_versions(flask_app)



# Globals
# -----------------------------------------------------



# App code
# -----------------------------------------------------
@flask_app.route('/')
def root():
    return 'Root page'

@flask_app.route('/version')
def version():
    return config['version']


# Helper functions
# -----------------------------------------------------

