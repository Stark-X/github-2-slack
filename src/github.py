import logging
import os

from flask import request, current_app

from src import utils
from src.authenticator.authenticator import AuthStrategy
from src.errors.exceptions import business


class GithubRequest(AuthStrategy):
    @staticmethod
    def is_enable():
        return current_app.config.get("AUTH")

    @staticmethod
    def auth():
        if GithubRequest.is_enable():
            GithubRequest.exec_auth()

    @staticmethod
    def exec_auth():
        sign = GithubRequest._extract_sign()
        secret = GithubRequest._get_secret()
        payload = "" if request.json is None else request.json
        remote_sign = utils.get_signature(secret, payload)
        if utils.verify_signature(sign, remote_sign) is False:
            logging.error("signature authorization failure")
            raise business.AUTH_ERROR

    @staticmethod
    def _extract_sign():
        signature = request.headers.get("X-Hub-Signature-256")
        if signature is None:
            logging.error("header not found")
            raise business.AUTH_ERROR
        return signature.split(":")[1].strip()

    @staticmethod
    def _get_secret():
        ret = os.environ.get("GITHUB_SECRET")
        if ret is None:
            logging.error("env config not found")
            raise business.AUTH_ERROR
        return ret
