import os

class Config:
    '''
    General configparent class
    '''

    SECRET_KEY = os.environ.get('SECRET_KEY') # k0ccMLjL5Eg2IzrpMb2zmfVLW6tUUYZA

    # Email configuration
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # SimpleMDE Config
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    # Database config
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://miro:password@localhost/pitches'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    Debug = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}