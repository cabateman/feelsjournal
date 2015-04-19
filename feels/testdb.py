import sys
from os import path

APP_ROOT = path.abspath(path.join(path.dirname(__file__), '..'))
sys.path.insert(1, APP_ROOT)

from feels import db
from feels.models import Emotion
import logging

e = Emotion()
result = e.get_by_name("happy")
print result
