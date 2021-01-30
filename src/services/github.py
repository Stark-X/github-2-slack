from src.factory import slack_client
from . import strategies
from .actions.unsupported import UnSupportedAction


class EventDispatcher(object):
    def dispatch(self, payload: dict) -> str:
        action_name = self.extract_action(payload)
        action_cls = strategies.get(action_name)
        if action_cls is None:
            action = UnSupportedAction(action_name)
        else:
            action = action_cls(payload)
        message_blocks = action.gather_formatted_message()
        title = action.build_title()
        return slack_client.send_message("#blog", title, message_blocks)

    @staticmethod
    def extract_action(payload: dict) -> str:
        return payload.get("action")
