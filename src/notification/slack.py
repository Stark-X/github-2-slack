from __future__ import annotations

import logging
from typing import List

from flask import Flask
# noinspection PyProtectedMember
from flask import _app_ctx_stack as stack
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from src.errors.exceptions import business
from src.errors.exceptions.business import REMOTE_ERROR

CONFIG_KEY = "SLACK_SECRET"


class SlackClient(object):
    def __init__(self, app: Flask = None):
        self.app = app
        self._token = None
        if app is not None:
            self.init_app(app)

    @property
    def connection(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, "slack_adaptor"):
                ctx.slack_adaptor = self.connect()
            return ctx.slack_adaptor

    def connect(self):
        return WebClient(token=self._token)

    def send_message(self, channel: str, msg: str, blocks: List[dict] = None) -> str:
        try:
            response = self.connection.chat_postMessage(channel=channel, text=msg, blocks=blocks)
            return response["message"]["text"]
        except SlackApiError as e:
            logging.error(f"slack failed: {e}")
            raise REMOTE_ERROR

    def teardown(self, exception):
        pass

    def init_app(self, app):
        token = app.config.get(CONFIG_KEY)
        if token is None:
            app.logger.error(f"no envvar for {CONFIG_KEY}")
            raise business.AUTH_ERROR
        self._token = token
        app.teardown_appcontext(self.teardown)
