class BizException(Exception):
    def __init__(self, code: int = 500, message: str = "unknown error"):
        self.code = code
        self.message = message

    def get_resp(self):
        return {
            "code": self.code,
            "message": self.message
        }


AUTH_ERROR = BizException(401, "auth error")
REMOTE_ERROR = BizException(500, "remote error")
