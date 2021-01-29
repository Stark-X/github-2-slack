from abc import ABCMeta


class AuthStrategy(metaclass=ABCMeta):
    @staticmethod
    def is_enable():
        return False

    @staticmethod
    def exec_auth():
        pass

    @staticmethod
    def auth():
        pass
