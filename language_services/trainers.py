__author__ = 'matt.livingston'
import nltk
from nltk.corpus import brown
from nltk.corpus import reuters
from pickle import dump
import threading
from multiprocessing import Process, Event
from time import sleep
import time
import datetime

#brown_tagged_sents = brown.tagged_sents(categories = 'news')
#brown_sents = brown.sents(categories='news')
#unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
#items = unigram_tagger.tag(brown_sents[2007])

#for t in items:
#    print(t)


#print(unigram_tagger.evaluate(brown_tagged_sents))


class TaggerModels:
    """
       Training and Test Models
        Corpora:
            Brown Corpus: The Brown Corpus was the first million-word electronic corpus
                        Created in 1961 at Brown University, it contains the text from
                        500 sources, categorized by genre (news,editorial, etc).
            Reuters Corpus: The Rueters Corpus contains 10,788 news docs totaling 1.3 million
                        words. They have been classified into 90 topics and grouped into two
                        sets called training and test.
            Gutenberg Corp: 18 texts, 2 Million words
    """
    def get_training_test_sentences(self):
        brown_cats = ",".join(brown.categories())
        self.news_text = brown.words(categories= brown.categories())
        self.news_tagged_sentences = brown.tagged_sents(categories= brown.categories())

        size = int(len(self.news_tagged_sentences) * .9)
        brown_train = self.news_tagged_sentences[:size]
        brown_test = self.news_tagged_sentences[size:]

        self.train_sents = brown_train
        self.test_sents  = brown_test



    def train_tagger(self):
        self.default_tagger = nltk.DefaultTagger('NN')
        self.unigram_tagger = nltk.UnigramTagger(self.train_sents, backoff=self.default_tagger)
        self.bigram_tagger = nltk.BigramTagger(self.train_sents, backoff=self.unigram_tagger)

        output = open('alfred_tagger.pkl', 'wb')
        dump(self.bigram_tagger, output, -1)
        output.close()


    def evaluate_unigram_tagger(self):
        return self.bigram_tagger.evaluate(self.news_tagged_sentences)

    def save_model(self):
        pass



"""
    Generate Training Models

"""

def run_trainer():
     tm = TaggerModels()
     tm.get_training_test_sentences()
     tm.train_tagger()
     print(tm.evaluate_unigram_tagger())



if __name__ == '__main__':
    run_trainer()