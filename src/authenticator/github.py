import os

from flask import request, current_app

from src import utils
from src.authenticator.authenticator import AuthStrategy
from src.errors.exceptions import business


class GithubAuth(AuthStrategy):
    @staticmethod
    def is_enable():
        return current_app.config.get("AUTH")

    @staticmethod
    def auth():
        if GithubAuth.is_enable():
            GithubAuth.exec_auth()

    @staticmethod
    def exec_auth():
        sign = GithubAuth._extract_sign()
        secret = GithubAuth._get_secret()
        payload = "" if request.json is None else request.json
        remote_sign = utils.get_signature(secret, payload)
        if utils.verify_signature(sign, remote_sign) is False:
            current_app.logger.warn("signature authorization failure")
            raise business.AUTH_ERROR

    @staticmethod
    def _extract_sign():
        signature = request.headers.get("X-Hub-Signature-256")
        if signature is None:
            current_app.logger.warn("header not found")
            raise business.AUTH_ERROR
        return signature.split(":")[1].strip()

    @staticmethod
    def _get_secret():
        ret = os.environ.get("GITHUB_SECRET")
        if ret is None:
            current_app.logger.error("env config not found")
            raise business.AUTH_ERROR
        return ret
