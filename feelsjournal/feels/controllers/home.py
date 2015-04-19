from flask import Blueprint
from feels import twilio_client

blueprint = Blueprint('home', __name__)


@blueprint.route("/", methods=['GET'])
def index():
    return "It works."

@blueprint.route("/welcome", methods=['GET'])
def welcome():
    message = twilio_client.messages.create(to="+19163371920", from_="+14153902961",
                                     body="Welcome to FeelsJournal!")
    return "Sending welcome message."
