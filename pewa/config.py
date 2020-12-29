import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DefaultConfig(object):
    SECRET_KEY = 'secret-key'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    AT_USERNAME = os.environ.get('AT_USERNAME')
    AT_API_KEY = os.environ.get('AT_API_KEY')
    AT_SENDER_ID = os.environ.get('AT_SENDER_ID')
    SESSION_TYPE = 'sqlalchemy'


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' +
                               os.path.join(basedir, 'dev.sqlite'))


class TestConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' +
                               os.path.join(basedir, 'test.sqlite'))
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    DEBUG = True

config_env_files = {
    'test': 'pewa.config.TestConfig',
    'development': 'pewa.config.DevelopmentConfig',
}
