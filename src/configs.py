class Config(object):
    DEBUG = False
    TESTING = False
    AUTH = True


class Development(Config):
    DEBUG = True
    AUTH = False
