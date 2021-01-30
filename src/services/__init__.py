from .actions.deployment_status import DeploymentAction
from .actions.push import PushAction

strategies = {"push": PushAction, "deployment_status": DeploymentAction}
