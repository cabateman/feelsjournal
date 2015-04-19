from flask import Blueprint
from feels import twilio_client

blueprint = Blueprint('home', __name__)


@blueprint.route("/", methods=['GET'])
def index():
    message = twilio_client.messages.create(to="+19163371920", from_="+14153902961",
                                     body="Hello there!")
    return "It works."
