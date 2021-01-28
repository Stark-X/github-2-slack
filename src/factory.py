import os

from flask import Flask

from src.errors.exceptions.business import BizException
from src.errors.register import handle_un_auth_error


def create_app():
    app = Flask(__name__)
    from .configs import Config
    app.config.from_object(Config)
    conf_name = os.environ.get("CONFIG_FILE")
    if conf_name is not None:
        app.config.from_json(conf_name)

    app.register_error_handler(BizException, handle_un_auth_error)

    return app
