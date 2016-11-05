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

from namyasto import app_path, project_path
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
        config_path = os.path.join(project_path, 'config', env + '.json')
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
    db_name = os.environ['DB_NAME']
    db_connect_str = 'sqlite:///db/{}'.format(db_name)

    flask_app = Flask(__name__)
    flask_app.secret_key                                = 'TTS96tKYthZh2V2jO7Bwi1c4BO0BFYfe8YnDegkg'
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False
    flask_app.config['SQLALCHEMY_DATABASE_URI']         = db_connect_str
    flask_app.config['DB_NAME']                         = db_name
    return flask_app

def register_versions(flask_app):
    flask_app.register_blueprint(app_v1_0_0, url_prefix='/v1_0_0')
    #flask_app.register_blueprint(current_app)
    current_app

def load_data(flask_app, db):
    db_path = os.path.join(app_path, 'db', flask_app.config['DB_NAME'])
    reset_db(db_path, db)

    return db_path

def reset_db(db_path, db):
    try:
        os.remove(db_path)
    except OSError:
        pass

    touch(db_path)
    from namyasto.db.models.person import Person
    db.create_all()
    db.session.commit()

def load_fixtures():
    data_path = os.path.join(app_path, 'db', 'fixtures', 'data.csv')


def touch(path):
    with open(path, 'a'):
        os.utime(path, None)
