__author__ = 'matt.livingston'

from speech.alfred_speech import AlfredSpeech
from utils.language import Core
from weather_services import weather
import nltk
from nltk import load_parser

print('Initializing Speech Engine')
alfred = AlfredSpeech()
language_processor = Core()

print('Loading Grammar Models')
weather_grammar = nltk.data.load('file:/config/simple_weather.cfg')
#text = "What is the weather?"
#d = language_processor.get_pos(text)


#cp = load_parser('/config/weather.fcfg')
# query = 'What cities are in China'
# trees = list(cp.parse(query.split()))

#for t in trees:
#    print(t)

#text = "What is the weather"
#text = "What is the current temp"
#text = "What is the current temperature"
#text = "What is tomorrow's forecast"
#text = "What will the weather be like tomorrow"
#tagged_text = language_processor.get_pos(text)

def get_weather_forecast(tree):
    for t in tree:
        t1 = t

    verb_phrase = t[1]

    weather_request = False
    tomorrow = False
    current = False

    for vp in verb_phrase:
        if 'weather' in vp:
            weather_request = True
        if 'tomorrow' in vp or "tomorrow's" in vp:
            tomorrow = True
        if 'current' in vp:
            current = True

    if current or (weather_request and not tomorrow):
        f = weather.Forecast("oswego, il")
        alfred.respond(f.get_todays_forecast())
        print(f.get_todays_forecast())
    elif tomorrow:
        f = weather.Forecast("oswego, il")
        print(f.get_specific_day('tomorrow'))
        alfred.respond(f.get_specific_day('tomorrow'))


def parse_input_for_grammar_tree(text):
    tree = None
    if 'weather' in text or 'temp' in text or 'forecast' in text or 'temperature' in text:
        sent = text.lower()
        sent = sent.split()
        rd_parser = nltk.RecursiveDescentParser(weather_grammar)
        tree = rd_parser.parse(sent)
        get_weather_forecast(tree)
    else:
        print("No Comprende")




while True:
    inp = input()   # Get the input
    try:
        parse_input_for_grammar_tree(inp)
    except:
        print("I do not understand the words coming out of your mouth")
        pass



"""
def parse_for_commands(text):
    pos = language_processor.get_pos(text)
    results = []
    for key, value in Commands.KEYWORDS.items():
        for t in pos:
            if t[0] == key:
                results.append(t[0])

    return results


while True:
    inp = input()   # Get the input
    commands = parse_for_commands(inp)

    if 'alfred' in inp:
        alfred.respond("Yes, sir?")
    elif 'toggl' in inp:
        alfred.respond("Certainly, Sir.")
        alfred.respond("Give me your hours break down please")
    elif 'weather' in inp:
        f = weather.Forecast("oswego, il")
        alfred.respond(f.get_todays_forecast())
    elif 'weather tomorrow' in inp:
        print('Tomorrow')
        f = weather.Forecast("oswego, il")
        alfred.respond(f.get_specific_day('tomorrow'))
    else:
        print('No command recognized')



clear = lambda: os.system('cls')


def drawProgressBar(engine, percent, barLen = 20):
    sys.stdout.write("\r")
    progress = ""
    for i in range(barLen):
        if i < int(barLen * percent):
            progress += "="
        else:
            progress += " "
    sys.stdout.write("Initializing [ %s]  [ %s ] %.2f%%" % (engine, progress, percent * 100))


for i in range(100):
    drawProgressBar("Language Engine", 1, 100)
    time.sleep(.01)

for i in range(100):
    drawProgressBar("Language Models", 1, 100)
    time.sleep(.01)

for i in range(100):
    drawProgressBar("Directive Protocols", 1, 100)
    time.sleep(.01)

sys.stdout.flush()

while True:             # Loop continuously
    inp = input()   # Get the input
    if inp == "Alfred?":       # If it is a blank line...
        alfred.respond("Yes, sir?")
    elif inp == "Update Toggl for me please.":
        alfred.respond("Certainly, Sir.")
        alfred.respond("Give me your hours break down please")
        inp = input()
        print(inp)
    elif inp == "You can sleep now":
        alfred.respond("Good night, sir")
        break           # ...break the loop
"""

