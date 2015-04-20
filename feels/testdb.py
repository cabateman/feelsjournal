import sys
from os import path

APP_ROOT = path.abspath(path.join(path.dirname(__file__), '..'))
sys.path.insert(1, APP_ROOT)

from feels import db
from feels.models import Emotion
import logging

with open("convertcsv.csv", "rb") as lines:
    for line in lines:
        emotions = line.strip().lower().split(",")
        for em in emotions:
            if len(em)>0:
                try:
                    e = Emotion(em)
                    e.save() 
                except:
                    pass
    

#e = Emotion()
#result = e.get_by_name("happy")
#print result
