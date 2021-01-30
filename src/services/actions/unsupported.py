from typing import List

from src.services.actions.action import GithubAction


class UnSupportedAction(GithubAction):
    def __init__(self, action: str):
        super().__init__()
        self._action_name = action

    def build_title(self):
        return f"unsupported event [{self._action_name}] triggered"

    def gather_formatted_message(self) -> List[dict]:
        return [
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"{self.build_title()}"
                    },
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"action *[{self._action_name}]* is unsupported yet :sweat_smile:"
                }
            }
        ]
