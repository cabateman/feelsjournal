from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import *
from twilio.rest import TwilioRestClient

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = PSQL_URL
db = SQLAlchemy(app)

twilio_client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

from feels.models import *
from feels.controllers import home, sms
from flask.ext.cors import CORS, cross_origin

""" Setup CORS
"""
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(home.blueprint)
app.register_blueprint(sms.blueprint)
