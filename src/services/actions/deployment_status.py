from typing import List

from .action import GithubAction


class DeploymentAction(GithubAction):
    def gather_formatted_message(self) -> List[dict]:
        url = self.payload["deployment"]["url"]
        return [
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"{self.build_title()}",
                    },
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"A new blog publish has been processing! :partying_face: :the_horns: :partying_face:\n [DEPLOYMENT]({url})",
                }
            }
        ]
