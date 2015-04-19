from flask import Blueprint, request
from feels import twilio_client
import twilio.twiml
import logging

blueprint = Blueprint('sms', __name__)

@blueprint.route("/incoming", methods=['POST'])
def sms():
    response = twilio.twiml.Response()
    body = request.form['Body']
    logging.debug("request received: {}".format(request.form))
    if "hi" in body.lower():
        response.sms("Hello there.")
    return str(response)
