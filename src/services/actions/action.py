from abc import ABCMeta
from typing import List


class GithubAction(metaclass=ABCMeta):
    def __init__(self, payload: dict = None):
        self._payload = payload

    @property
    def payload(self):
        return self._payload

    def build_title(self):
        return f"[{type(self).__name__}] triggered :smirk:"

    def gather_formatted_message(self) -> List[dict]:
        pass
