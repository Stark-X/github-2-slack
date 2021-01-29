from src.authenticator.decorator import auth
from src.factory import create_app
from src.authenticator.github import GithubAuth

app = create_app()


@app.route("/")
@auth.pre_auth(GithubAuth)
def hello():
    return "Hello World!"
