import os

class Config:
    '''
    parent class configuration
    '''
    NEWS_API_SOURCE_URL='https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    CATEGORY_API_URL='https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'




class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Child class development configuration
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}