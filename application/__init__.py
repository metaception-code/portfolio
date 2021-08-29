# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import Flask


def register_blueprints(app):
    from application.views.base import base_blueprint
    from application.views.projects import project_blueprint
    app.register_blueprint(base_blueprint)
    app.register_blueprint(project_blueprint)


def create_app(extra_config_settings: dict = {}):
    # Basic configuration

    app = Flask(__name__, static_folder='static')
    # Load settings from './settings.py'
    app.config.from_object('application.settings')
    # Load local settings from './local_settings.py'
    app.config.from_object('application.local_settings')
    # Load extra config settings from 'extra_config_settings' param
    app.config.update(extra_config_settings)
    if 'SECURITY_PASSWORD_SALT' not in app.config:
        app.config['SECURITY_PASSWORD_SALT'] = app.config['SECRET_KEY']

    # Base blueprints
    register_blueprints(app)

    # Register error handlers
    from application.views.errors import page_not_found
    app.register_error_handler(404, page_not_found)

    return app
