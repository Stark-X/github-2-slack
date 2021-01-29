class DefaultConfig(object):
    FLASK_ENV = "production"
    TESTING = False
    AUTH = True
    LOG_FORMAT = "[%(asctime)s] [%(remote_addr)s] %(levelname)s in %(module)s.%(funcName)s(l:%(lineno)s): %(message)s"
