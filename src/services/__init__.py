from .actions.deployment import DeploymentAction
from .actions.push import PushAction

strategies = {"push": PushAction, "deployment": DeploymentAction}
