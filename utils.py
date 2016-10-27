__author__ = 'peter'

import csv
import itertools
import numpy as np
import nltk
import time
import sys
import operator
import io
import array
from datetime import datetime
from GRU_tutorial import GRUTheano
import scrapeAuthors as gbData


SENTENCE_START_TOKEN = "SENTENCE_START"
SENTENCE_END_TOKEN = "SENTENCE_END"


def prepairData():

    vocab, sentences = gbData.janeAusten()

    #preume did main function of scrapeAuthors
    #have vocab DF of words, their index

    #reset index, then just convert to dict over word and index fields
    #set index to word, then con

    vocab.reset_index(1,inplace=True)
    index_to_word = vocab['word'].to_dict()
    #index_to_word = ["<MASK/>", UNKNOWN_TOKEN] + [x[0] for x in sorted_vocab]
    del vocab['index']
    vocab.reset_index(inplace = True)
    wordIndexedVocab = vocab.set_index('word')
    word_to_index = wordIndexedVocab['index'].to_dict()
    #word_to_index = dict([(w, i) for i, w in enumerate(index_to_word)])

    # Replace all words not in our vocabulary with the part of speach
    for i, sent in enumerate(sentences):
        for word in sent:
            if word[0] in word_to_index.keys():
                word = word[0]
            elif word[1] in word_to_index.keys():
                word = word[1]
            else:
                word = 'Token'

        tokenized_sentences[i] = [w[0] if w[0] in word_to_index.keys() else w[1] for w in sent]

    # Create the training data
    X_train = np.asarray([[word_to_index[w] for w in sent[:-1]] for sent in tokenized_sentences])
    y_train = np.asarray([[word_to_index[w] for w in sent[1:]] for sent in tokenized_sentences])

    return X_train, y_train, word_to_index, index_to_word

def load_data(TRAINING_CORPUS):
    return x_train, y_train, word_to_index, index_to_word