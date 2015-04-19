from flask import Blueprint, request
from feels import twilio_client, Users
import twilio.twiml
import logging

blueprint = Blueprint('sms', __name__)

@blueprint.route("/incoming", methods=['POST'])
def sms():
    response = twilio.twiml.Response()
    body = request.form['Body'].lower()
    phone_number = request.form['From']
    logging.debug("request received: {}".format(request.form))

    # get user_id from phone_number
    user = Users.get_by_phone_number(phone_number) 
    user_id = user.id
    new_user = False
    if user_id is None:
        user = Users.create(phone_number) 
        user_id = user.id
        new_user = True

    if "hi" in body and new_user:
        response.sms("How are you feeling today? Type 'help' for options.")
    elif "hi" in body:
        response.sms("How are you feeling today?")

    if "help" in body:
        response.sms("[emotion] - type your emotion to journal. ex 'anger'\n \
                      list - list common emotions\n \
                      less - reduce survey freq\n \
                      more - increase survey freq\n \
                      stop - stop all messages\n \
                      ")

    return str(response)
