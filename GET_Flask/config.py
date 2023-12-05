from datetime import timedelta

class Config(object):
    """Base config, uses staging database server."""


    SITE_DOMAIN='https://dev.thisisget.com'

  
    MONGO_DB='TEST_GET'

    # A Fake Amount in the Plaid Sandbox Account    
    TEST_INVESTOR_BALANCE = True
    TEST_INVESTOR_BALANCE_AMOUNT = 1000000000

    #update in Nuxt too
    TRANSACTION_LIMIT = 5000

    # JWT
    JWT_COOKIE_SECURE=False
    JWT_TOKEN_LOCATION=["cookies"]
    JWT_SECRET_KEY="xxx"
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(hours=1)
    JWT_COOKIE_CSRF_PROTECT=True
    JWT_CSRF_IN_COOKIES=True
    JWT_COOKIE_SAMESITE="Lax"
    

class SandboxConfig(Config):

    ENV='sandbox'
    TEMPLATES_AUTO_RELOAD=True

    TEST_PLAID_RUX = True




class DevelopmentConfig(Config):

    ENV='development'
    TEMPLATES_AUTO_RELOAD=True


    TEST_PLAID_RUX = False


class ProductionConfig(Config):

    ENV='production'
    TEST_PLAID_RUX = False

    SITE_DOMAIN='https://dev.thisisget.com'

    MONGO_DB='GET_X'

    # JWT
    JWT_COOKIE_SECURE=True
    JWT_SECRET_KEY="xxxx"

    TEST_INVESTOR_BALANCE = False
    #update in Nuxt too
    TRANSACTION_LIMIT = 100000


    TEST_EMAIL_RECIPIENTS = False

    