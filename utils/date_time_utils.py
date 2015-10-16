__author__ = 'matt.livingston'

import datetime

class SpeechHelpers:

    def determine_greeting(self,x):
        if x.hour >= 6 and x.hour < 12:
            return 'Morning'
        if x.hour >= 12 and x.hour < 18:
            return 'Afternoon'
        else:
            return "Evening"

