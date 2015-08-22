__author__ = 'matt.livingston'
"""
Good Resource: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
Tag     Description                                     Example
WP:     Wh-pronoun                                      Who, What, When, Where
MD:     Modal                                           will
VMZ:    Verb, 3rd person singular present               is, tomorrows
DT:     Determiner                                      the
JJ:     Adjective                                       current
NN:     Noun, singular or mass                          weather, temp, temperature, Wednesday
VB:     Verb, base form                                 be
IN:     Preposition or subordinating conjunction        like
VBN:    Verb, past particle                             forecast
.:      Punctuation Mark
"""


simple_weather_grammar = """
S -> WP VP
VP -> VBZ DT NN | VBZ NN
VBZ -> "is" | "tomorrow's"
DT -> "the"
JJ -> "current" | "next"
NN -> "weather" | "temp" | "temperature" | "weather"
VB -> "be"
IN -> "like"
VBN -> "forecast"
"""



def simple_weather_grammar():
    return simple_weather_grammar

