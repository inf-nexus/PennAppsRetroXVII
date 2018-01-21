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
        description = document['description']


        # content = [re.findall(r'\w+', c) for c in sent_tokenize(content.lower())]
        temp_description = []
        if isinstance(description, str):
            for c in sent_tokenize(description.lower()):
                temp_description.append(re.findall(r'\w+', c))

        # tagline = [re.findall(r'\w+', t) for t in sent_tokenize(tagline.lower())]
        temp_tagline = []
        if isinstance(tagline, str):
            for t in sent_tokenize(tagline.lower()):
                temp_tagline.append(re.findall(r'\w+', t))

        data_pp.append(document)

        data_pp[-1]['tagline'] = temp_tagline
        data_pp[-1]['description'] = temp_description

    return data_pp


class MagicModel(object):

    def __init__(self, data):
        self.data = data
        self.init_model()

    def extract_relevant_fields(self):
        # result = []
        # for document in self.data:
        #     for word in document['tagline']:

        # for document in self.data:
            # print(type(document['tagline']))
            # print(document['tagline'])
            # print(type(document['description']))
            # print(document['description'])

        result = []
        for document in self.data:
            for word in document['tagline']:
                result.append(word)

            for word in document['description']:
                result.append(word)


        # return [document['tagline'] + document['description'] for document in self.data]
        return result




    @timeme
    def init_model(self):
        # model_dict = {}
        # if (os.path.isfile('model.p')):
        #     model_dict = pickle.load(open('model.p', 'rb'))
        # else:
        #     model_dict['dictionary'] = gensim.corpora.Dictionary(self.extract_relevant_fields())
        #     model_dict['corpus'] = [self.dictionary.doc2bow(document) for document in self.extract_relevant_fields()]
        #     model_dict['tf_idf'] = gensim.models.TfidfModel(self.corpus)
        #     model_path = os.path.join(os.getcwd(), 'models')
        #     model_dict['model'] = gensim.similarities.Similarity(model_path, self.tf_idf, num_features=len(self.dictionary))
        #     pickle.dump(model_dict, open('model.p', 'wb'))
        #
        # self.dictionary = model_dict['dictionary']
        # self.corpus = model_dict['corpus']
        # self.tf_idf = model_dict['tf_idf']
        # self.model = model_dict['model']

        self.dictionary = gensim.corpora.Dictionary(self.extract_relevant_fields())
        self.corpus = [self.dictionary.doc2bow(document) for document in self.extract_relevant_fields()]
        self.tf_idf = gensim.models.TfidfModel(self.corpus)
        model_path = os.path.join(os.getcwd(), 'models')
        self.model = gensim.similarities.Similarity(model_path, self.tf_idf[self.corpus], num_features=len(self.dictionary))
        # pickle.dump(self.model, open('model.p', 'wb'))


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
