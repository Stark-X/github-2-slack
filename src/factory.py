
from flask import Flask
from flask.logging import default_handler

from src.errors.exceptions.business import BizException
from src.errors.register import handle_un_auth_error


def create_app():
    app = Flask(__name__)
    init_config(app)
    init_logger(app)

    app.register_error_handler(BizException, handle_un_auth_error)

    return app


def init_logger(app):
    import logging
    log_format = app.config.get("LOG_FORMAT")
    if log_format is not None:
        default_handler.setFormatter(logging.Formatter(log_format))


def init_config(app):
    from .configs import DefaultConfig
    app.config.from_object(DefaultConfig)
    import os
    conf_name = os.environ.get("CONFIG_FILE")
    if conf_name is not None:
        app.config.from_json(conf_name)
