import os
import json

import numpy as np

import gensim

from nltk.tokenize import sent_tokenize, word_tokenize
import re

import time

import pickle


def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time() * 1000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 1000))

        print(method.__name__, endTime - startTime, 'ms')
        return result

    return wrapper


@timeme
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

@timeme
def preprocess_data(data):
    data_pp = []

    for document in data:
        tagline = document['tagline']
        content = document['description']

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
        return [document['tagline'] + document['description'] for document in self.data]


    @timeme
    def init_model(self):
        if (os.path.isfile('model.p')):
            self.model = pickle.load(open('model.p', 'rb'))
        else:
            self.dictionary = gensim.corpora.Dictionary(self.extract_relevant_fields())
            self.corpus = [self.dictionary.doc2bow(document) for document in self.extract_relevant_fields()]
            self.tf_idf = gensim.models.TfidfModel(self.corpus)
            model_path = os.path.join(os.getcwd(), 'models')
            self.model = gensim.similarities.Similarity(model_path, self.tf_idf, num_features=len(self.dictionary))
            pickle.dump(self.model, open('model.p', 'wb'))


    def calc_similarity(self, text, n_best=5, threshold=0.0):
        prediction = self.model[self.convert2tfidf(text)]

        sorted_predictions = sorted(enumerate(prediction), key=lambda x: x[1], reverse=True)

        if len(sorted_predictions) < n_best:
            for i, elem in enumerate(sorted_predictions):
                if elem[1] < threshold:
                    return sorted_predictions[:i]
            return sorted_predictions
        else:
            for i, elem in enumerate(sorted_predictions):
                if elem[1] < threshold:
                    return sorted_predictions[:i]
            return sorted_predictions[:n_best]


    def convert2tfidf(self, text):
        query_doc = [w.lower() for w in word_tokenize(text)]
        query_doc_bow = self.dictionary.doc2bow(query_doc)
        query_doc_tf_idf = self.tf_idf[query_doc_bow]

        return query_doc_tf_idf


def main():
    filepath = os.path.join(os.getcwd(), 'data')

    data_raw = load_data(filepath)
    data_preprocessed = preprocess_data(data_raw)
    model = MagicModel(data_preprocessed)

    return model

if __name__ == '__main__':
    main()
