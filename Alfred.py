__author__ = 'matt.livingston'

from speech import alfred_speech


alfred_speech_service = alfred_speech.AlfredSpeech()

alfred_speech_service.respond("yes sir?")

rules = {
    "Alfred": "yes sir?",
    "What is the current temperature?": "The current temperature is %s",
    "Add 8 hours to Toggl for the Hancock Project ": "yes sir"

}