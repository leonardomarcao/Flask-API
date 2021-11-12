# -*- coding: utf-8 -*-
import os


class Config:

    # project root directory
    BASE_DIR = os.path.join(os.pardir, os.path.dirname(__file__))
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # Flask Configuration
    # --------------------------------------------------------------------
    DEBUG = False
    TESTING = False
    PORT = 8000

    # log file path
    # --------------------------------------------------------------------
    enable_access_log = False
    log_socket_host = "127.0.0.1"
    log_socket_port = 514


class DevelopmentConfig(Config):

    ENV = os.environ.get("FLASK_ENV", "development")
    DEBUG = True
    ASSETS_DEBUG = True


class TestingConfig(Config):

    ENV = os.environ.get("FLASK_ENV", "testing")
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):

    ENV = os.environ.get("FLASK_ENV", "production")
    DEBUG = False
    USE_RELOADER = False


settings = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
