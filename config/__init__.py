import logging
from os import path
import os

APP_ROOT = path.abspath(path.join(path.dirname(__file__), '../'))

# Logging
LOGGING_LEVEL = logging.DEBUG
LOGGING_ADDRESS = "/var/log/feelsjournal"  # don't use syslog if its None

# API Version
API_VERSION = "1.0"

############ 
# Postgres
############ 

# Bind - payment
PSQL_HOST = 'localhost'
PSQL_DATABASE = 'textfeel'
PSQL_USER = ''
PSQL_PASSWORD = ''
PSQL_PORT = '5432'

#############
# Twilio
#############
TWILIO_ACCOUNT_SID = "ACcd5837cbfe0b2a7b79a4aeb04e8f0e17"
TWILIO_AUTH_TOKEN = "b8c8a53b8f498cb65ac4b34e614f8e61"

# create a config.py to override above settings
try:
    from config_staging import *
except ImportError:
    pass

#####################################
# Initializations based on configs
#####################################

PSQL_URL = "postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{database}".format(
            user=PSQL_USER,
            passwd=PSQL_PASSWORD,
            host=PSQL_HOST,
            port=PSQL_PORT,
            database=PSQL_DATABASE)
