import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	"""
	Common configurations
	"""

	# Put any configurations here that are common across all environments

	HOST = '0.0.0.0'
	SECRET_KEY = 'CHANGEME'


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False



app_config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig
}
