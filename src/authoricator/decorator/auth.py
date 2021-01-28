import functools
from typing import Type

from src.authoricator.authoricator import AuthStrategy


def pre_auth(strategy: Type[AuthStrategy]):
    def decorate(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            strategy.auth()
            return func(*args, **kwargs)

        return wrapper

    return decorate
