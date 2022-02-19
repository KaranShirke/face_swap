class Config(object):

    SECURET_KEY = 'asphalt8'

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None

class DevelopmentConfig(Config):
    DEBUG = True