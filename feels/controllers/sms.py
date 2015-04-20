from flask import Blueprint, request, jsonify
from feels import twilio_client, Users, Emotion, Journal
import twilio.twiml
import logging

blueprint = Blueprint('sms', __name__)

@blueprint.route("/incoming", methods=['POST'])
def sms():
    response = twilio.twiml.Response()
    body = request.form['Body'].lower()

    # quick sanity check to make sure we have a payload
    if not body:
        return jsonify({"status":False})

    command = body.split()[0]

    phone_number = request.form['From']
    logging.debug("request received: {}".format(request.form))

    # get user_id from phone_number
    user = Users.get_by_phone_number(phone_number) 
    new_user = False
    if not user:
        user = Users.create(phone_number) 
        new_user = True
    user_id = user.id
    
    if "hi" == command and new_user:
        response.sms("How are you feeling today? Type 'help' for options.")
        return str(response)

    elif "hi" == command:
        response.sms("How are you feeling today?")
        return str(response)

    if "help" == command:
        response.sms("[emotion] - type your emotion to journal. ex 'anger'\n \
                      bc [description] - type reason for emotion. ex 'bc my car broke down'\n \
                      list - list common emotions\n \
                      less - reduce survey freq\n \
                      more - increase survey freq\n \
                      stop - stop all messages\n \
                      ")
        return str(response)

    if "list" == command:
        emotions = Emotion.get_all_csv()
        response.sms(emotions)
        return str(response)

    if "less" == command:
        num_daily_checkup = Users.decrease_daily_checkup(user)
        if num_daily_checkup == 1:
            response.sms("You are at the minimum daily checkup limit (1). Text 'stop' if you wish to temporarily stop checkups")
        else:
            response.sms("You have decreased your daily checkups to {}".format(num_daily_checkup))
        return str(response)

    if "more" == command:
        num_daily_checkup = Users.increase_daily_checkup(user)
        if num_daily_checkup == 10:
            response.sms("You are at the maximum daily checkup limit (10).")
        else:
            response.sms("You have increased your daily checkups to {}".format(num_daily_checkup))
        return str(response)

    if "stop" == command:
        Users.stop_daily_checkup(user)
        response.sms("You have stopped daily emotional checkups. Text 'hi' to checkin again.")
        return str(response)

    if "bc" == command:
        new_description = body[2:]
        if new_description:
            prev_journal = Journal.get_previous_journal(user)
            if prev_journal:
                Journal.add_description(prev_journal, body[2:].strip())
                response.sms("Noted!")
            else:
                response.sms("First say what you are feeling before you say why. ex. 'anger'")
        else:
            response.sms("Add more to your description. ex 'bc my car broke down'")
    else:  
        emotion_id = Emotion.get_id_by_search_terms(command)
        if emotion_id:
            Journal.create(user, emotion_id, command)
        else:
            e = Emotion.create(command)
            Journal.create(user_id, e.id, command)
        response.sms("Noted! Any reason why?")
          

    return str(response)
