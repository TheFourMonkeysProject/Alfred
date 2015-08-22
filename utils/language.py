__author__ = 'matt.livingston'
import nltk
from nltk import word_tokenize
from nltk.sem import extract_rels
from nltk.sem import rtuple
import re
import os
import binascii


class Core:

    def search(self, text, term):
        return text.concordance(term)

    def get_pos(self, text):
        tokenized_sentences = word_tokenize(text.lower())
        tagged_sentences = nltk.pos_tag(tokenized_sentences)
        return tagged_sentences

"""
Operator	Behavior
.	        Wildcard, matches any character
^abc	    Matches some pattern abc at the start of a string
abc$	    Matches some pattern abc at the end of a string
[abc]	    Matches one of a set of characters
[A-Z0-9]	Matches one of a range of characters
ed|ing|s	Matches one of the specified strings (disjunction)
*	        Zero or more of previous item, e.g. a*, [a-z]* (also known as Kleene Closure)
+	        One or more of previous item, e.g. a+, [a-z]+
?	        Zero or one of the previous item (i.e. optional), e.g. a?, [a-z]?
{n}	        Exactly n repeats where n is a non-negative integer
{n,}	    At least n repeats
{,n}	    No more than n repeats
{m,n}	    At least m and no more than n repeats
a(b|c)+	    Parentheses that indicate the scope of the operators
"""

# Detecting word patterns
class WordPatterns:
    def __init__(self):
        self.wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]

    def return_word_tokens(self, word_group, language):
        return word_tokenize(word_group)

    def find_ending_in(self, word_group, ending_in):
        word_list = self.return_word_tokens(word_group, 'en')

        endings = [w for w in word_list if re.search(ending_in + '$', w)]
        print(endings)

    # def find_beginning_in(self, word_group, beginning_in):

    """
    Normalizing Text: Stemmers
    """


class InformationExtraction:
    """
        Information Extraction Architecture
        1. Raw Text in
        2. Sentence Segmentation
        3. Tokenize each sentence
        4. POS tag each tokenized sentence
        5. Entity Detection
        6. Relation Detection


        This algorithm takes the raw text of a document as its input, and generates a list of (entity, relation, entity)
        tuples as it output.
    """
    def __init__(self):
        self.id = binascii.b2a_hex(os.urandom(15))

    """
        Preprocess the document
        1. Sentence Segmentation
        2. Tokenize each sentence
        3. POS Tag each sentence
    """
    def preprocess(self, document):
        print("Beginning Preproceesing of documnet")
        # Tokenize each sentence in the document
        sentences = nltk.sent_tokenize(document)
        print("Sentences have been tokenized")
        # Tokenize each word in each sentence
        self.tokenized_sentences = [nltk.word_tokenize(sent) for sent in sentences]
        print("Words have been tokenized")
        # POS Tag each sentence
        self.tagged_sentences = [nltk.pos_tag(sent) for sent in self.tokenized_sentences]
        print("Parts Of Speech (POS) tagging has completed")


    """
        Commonly Used Types of Named Entity
        NE Type	        Examples
        ORGANIZATION	Georgia-Pacific Corp., WHO
        PERSON	        Eddy Bonte, President Obama
        LOCATION	    Murray River, Mount Everest
        DATE	        June, 2008-06-29
        TIME	        two fifty a m, 1:30 p.m.
        MONEY	        175 million Canadian Dollars, GBP 10.40
        PERCENT	        twenty pct, 18.75 %
        FACILITY	    Washington Monument, Stonehenge
        GPE	            South East Asia, Midlothian
    """
    def entity_detection(self):
        # self.entities = [nltk.ne_chunk(word, binary=True) for word in self.tagged_sentences]
        #self.entities = [nltk.pos_tag(sentence) for sentence in self.tagged_sentences]
        print("Entity Detection complete.")
        print(self.entities)



    def relation_extraction(self):
        IN = re.compile(r'.*\bin\b(?!\b.+ing)')
        for doc in self.entities:
            for rel in nltk.sem.extract_rels('ORG', 'LOC', doc,
                                             corpus='ace', pattern = IN):
                print(nltk.sem.rtuple(rel))
        for i, sent in enumerate(self.tagged_sentences):
            sent = nltk.ne_chunk(sent) # ne_chunk method expects one tagged sentence
            rels = extract_rels('PER', 'ORG', sent, corpus='ace', pattern=IN, window=7) # extract_rels method expects one chunked sentence
            for rel in rels:
                print('{0:<5}{1}'.format(i, rtuple(rel)))

    def process(self, document):
        self.preprocess(document)
        self.entity_detection()
        self.relation_extraction()


doc = """The fourth Wells account moving to another agency is the packaged paper-products division of Georgia-Pacific
Corp.,which arrived at Wells only last fall. Like Hertz and the History Channel, it is also leaving for an Omnicom-owned
agency, the BBDO South unit of BBDO Worldwide. BBDO South in Atlanta, which handles corporate advertising for
Georgia-Pacific, will assume additional duties for brands like Angel Soft toilet tissue and Sparkle paper towels,
said Ken Haldin, a spokesman for Georgia-Pacific in Atlanta.
"""

# a = WordPatterns()
# a.find_ending_in("We were walking along the ending of the trail following the sentence.", "ing")
#b = InformationExtraction()
#b.process(doc)



#wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]

#print([w for w in wordlist if re.search('^..j..t..$', w)])

#chat_words = sorted(set(w for w in nltk.corpus.nps_chat.words()))

#print([w for w in chat_words if re.search('^[ha]+$', w)])


class Question:
    def __init__(self):
        pass


