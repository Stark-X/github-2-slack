from .exceptions.business import BizException


def handle_un_auth_error(err: BizException):
    return err.get_resp(), err.code
