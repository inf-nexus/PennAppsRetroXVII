import os
import json

import numpy as np

import gensim

from nltk.tokenize import sent_tokenize, word_tokenize
import re



def load_data(path):
    raw_data = []

    if os.path.isdir(path): # iterate over all files in directory
        for file in os.listdir(path):
            temp = json.load(open(os.path.join(path, file)))
            for elem in temp:
                raw_data.append(elem)

    elif os.path.isfile(path):  # filepath provided
        temp = json.load(open(path))
        for elem in temp:
            raw_data.append(elem)
    else:
        return None

    return raw_data


def preprocess_data(data):
    # lowercasing
    # Tokenizing
    # punctuation
    data_pp = []

    for document in data:
        tagline = document['tagline']
        content = document['description']

        # result = []
        # for sent in sent_tokenize(content.lower()):
        #     result.append(re.findall(r'\w+', sent))

        content = [re.findall(r'\w+', c) for c in sent_tokenize(content.lower())]
        tagline = [re.findall(r'\w+', t) for t in sent_tokenize(tagline.lower())]

        data_pp.append(document)

        data_pp[-1]['tagline'] = tagline
        data_pp[-1]['content'] = content

    return data_pp


class MagicModel(object):

    def __init__(self, data):
        self.data = data

        self.init_model()

    def extract_relevant_fields(self):
        pass

    def init_model(self):
        self.dictionary = gensim.corpora.Dictionary(self.extract_relevant_fields())
        self.corpus = None
        self.tf_idf = None
        self.model = None


    def calc_similarity(self, text):
        pass


    def convert2tfidf(self, text):
        pass


def main():
    filepath = os.path.join(os.getcwd(), 'data')

    data_raw = load_data(filepath)
    data_preprocessed = preprocess_data(data_raw)
    model = MagicModel(data_preprocessed)



if __name__ == '__main__':
    main()
