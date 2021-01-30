from flask import request, current_app

from src import utils
from src.authenticator.authenticator import AuthStrategy
from src.errors.exceptions import business

CONFIG_KEY = "GITHUB_SECRET"


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
        secret = GithubAuth._get_secret()
        local_sign = utils.get_signature(secret, request.get_data())

        from_header_sign = GithubAuth.extract_sign_from_header()
        if utils.verify_signature(from_header_sign, local_sign) is False:
            current_app.logger.warn("signature authorization failure")
            raise business.AUTH_ERROR

    @staticmethod
    def extract_sign_from_header():
        signature = request.headers.get("X-Hub-Signature-256")
        if signature is None:
            current_app.logger.warn("header not found")
            raise business.AUTH_ERROR
        splits = signature.split("=")
        return splits[1].strip() if len(splits) == 2 else ""

    @staticmethod
    def _get_secret():
        ret = current_app.config.get(CONFIG_KEY)
        if ret is None:
            current_app.logger.error("env config not found")
            raise business.AUTH_ERROR
        return ret
