from src.authenticator.decorator import auth
from src.factory import create_app
from src.github import GithubRequest

app = create_app()


@app.route("/")
@auth.pre_auth(GithubRequest)
def hello():
    return "Hello World!"
