"""Application configuration."""

import os


class Config(object):
    """Base config class."""

    SECRET_KEY = os.environ.get('SECRET_KEY')

class TestingConfig(Config):
    """Configuration for testing environment."""
    TESTING = True
    DEBUG = True

    db_url = "dbname='ireporter' host='localhost' port='5432' user='andela' password='pass123'"

class StagingConfig(Config):
    """Configurations for Staging environment"""
    DEBUG = True

class DevelopmentConfig(Config):
    """Configuration for development environment."""
    DEBUG = False
    db_url = "dbname='ireporter' host='localhost' port='5432' user='andela' password='pass123'"

class ProductionConfig(Config):
    """Configurations for production environment."""
    DEBUG = False
    TESTING = False 

configurations = {
    "testing": TestingConfig,
    "staging": StagingConfig,
    "development": DevelopmentConfig,
    "production" : ProductionConfig,
}
























