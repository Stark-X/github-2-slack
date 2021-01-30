import logging
import os
from pathlib import Path

from flask import Flask
from flask import has_request_context, request
from flask.logging import default_handler

from src.errors.exceptions.business import BizException
from src.errors.register import handle_un_auth_error
from src.notification import slack

DEFAULT_SECRET_CONF = "secret.json"

GITHUB_SECRET = "GITHUB_SECRET"
SLACK_SECRET = "SLACK_SECRET"

slack_client = slack.SlackClient()


def create_app():
    app = Flask(__name__)
    init_config(app)
    init_secrets(app)
    init_logger(app)
    slack_client.init_app(app)

    app.register_error_handler(BizException, handle_un_auth_error)

    return app


# noinspection StrFormat
class EnhancedFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        record.url = None
        record.remote_addr = None
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        return super().format(record)


def init_logger(app: Flask):
    log_format = app.config.get("LOG_FORMAT")
    if log_format is not None:
        default_handler.setFormatter(EnhancedFormatter(log_format))


def init_config(app: Flask):
    root_path = Path(app.instance_path).parent

    from .configs import DefaultConfig
    app.config.from_object(DefaultConfig)
    conf_name = os.environ.get("CONFIG_FILE")
    if conf_name is not None:
        app.logger.info(f"using config file '{conf_name}'")
        app.config.from_json(root_path.joinpath(conf_name))


def init_secrets(app):
    root_path = Path(app.instance_path).parent

    secret_conf_name = os.environ.get("SECRET_FILE", DEFAULT_SECRET_CONF)
    if secret_conf_name == DEFAULT_SECRET_CONF:
        app.logger.info(f"using default secret file '{DEFAULT_SECRET_CONF}'")
    secret_conf = root_path.joinpath(secret_conf_name)
    if not secret_conf.exists():
        app.logger.error(f"secret config file '{secret_conf}' not exists")
    app.config.from_json(secret_conf)

