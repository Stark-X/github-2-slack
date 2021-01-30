from typing import List

from .action import GithubAction


class PushAction(GithubAction):
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
                    "text": f"event *[{type(self).__name__}]* occurred~ :smirk:"
                }
            }
        ]
