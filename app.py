from flask import request

from src.authenticator.decorator import auth
from src.authenticator.github import GithubAuth
from src.factory import create_app, slack_client
from src.services.github import EventDispatcher

app = create_app()


@app.route("/")
@auth.pre_auth(GithubAuth)
def hello():
    return "Hello World!"


@app.route("/github", methods=["POST"])
@auth.pre_auth(GithubAuth)
def github():
    slack_client.send_message("#blog", "hi from github")
    dispatcher = EventDispatcher()
    print(dispatcher.dispatch(request.json))
    return "success"
