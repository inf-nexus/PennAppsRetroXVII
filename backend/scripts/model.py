import os
import json

import numpy as np

import gensim

from nltk.tokenize import word_tokenize
import re

import time

import pickle
import math


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

    if os.path.isdir(path):  # iterate over all files in directory
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

        temp_description = []
        if isinstance(description, str):
            temp_description = re.findall(r'\w+', description.lower())

        temp_tagline = []
        if isinstance(tagline, str):
            temp_tagline = re.findall(r'\w+', tagline)


        data_pp.append(document)

        data_pp[-1]['tagline'] = temp_tagline
        data_pp[-1]['description'] = temp_description

    return data_pp


class MagicModel(object):

    def __init__(self, data):
        self.data = data
        self.init_model()

    def extract_relevant_fields(self):
        return [document['tagline'] + document['description'] for document in self.data]

    @timeme
    def init_model(self):
        model_dict = {}
        if (os.path.isfile('model.p')):
            print('Loading from File')
            model_dict = pickle.load(open('model.p', 'rb'))
            self.dictionary = model_dict['dictionary']
            self.corpus = model_dict['corpus']
            self.tf_idf = model_dict['tf_idf']
            self.model = model_dict['model']
        else:
            extracted_features = self.extract_relevant_fields()
            self.dictionary = gensim.corpora.Dictionary(extracted_features)
            self.corpus = [self.dictionary.doc2bow(document) for document in extracted_features]
            self.tf_idf = gensim.models.TfidfModel(self.corpus)
            model_path = os.path.join(os.getcwd(), 'models')
            self.model = gensim.similarities.Similarity(model_path, self.tf_idf[self.corpus], num_features=len(self.dictionary))

            model_dict['dictionary'] = self.dictionary
            model_dict['corpus'] = self.corpus
            model_dict['tf_idf'] = self.tf_idf
            model_dict['model'] = self.model
            pickle.dump(model_dict, open('model.p', 'wb'))


    def calc_similarity(self, text, n_best=5, threshold=0.0):
        prediction = self.model[self.convert2tfidf(text)]

        sorted_predictions = sorted(enumerate(prediction), key=lambda x: x[1], reverse=True)

        # self.calculate_originality(sorted_predictions)
        # if len(sorted_predictions) < n_best:
        #     for i, elem in enumerate(sorted_predictions):
                # if elem[1] < threshold:
                    # return sorted_predictions[:i]
            # return sorted_predictions
        # else:
        #     for i, elem in enumerate(sorted_predictions):
        #         if elem[1] < threshold:
                    # return sorted_predictions[:i]
            # return sorted_predictions[:n_best]

        return [(self.data[pred[0]], pred[1]) for pred in sorted_predictions[:n_best]], self.calculate_originality(sorted_predictions)


        # return self.convert2readable(sorted_predictions[:n_best])

    def convert2readable(self, preds):
        return [" ".join(self.data[pred[0]]['tagline']) for pred in preds]

    def convert2tfidf(self, text):
        query_doc = [w.lower() for w in word_tokenize(text)]
        query_doc_bow = self.dictionary.doc2bow(query_doc)
        query_doc_tf_idf = self.tf_idf[query_doc_bow]

        return query_doc_tf_idf

    def calculate_originality(self, predictions):

        scores = []

        for elem in predictions[:10]:
            scores.append(elem[1])

        print(sum(scores)/len(scores))
        return sum(scores)/len(scores)




def getModel():
    filepath = os.path.join(os.getcwd(), 'data', 'json')

    data_raw = load_data(filepath)
    data_preprocessed = preprocess_data(data_raw)
    model = MagicModel(data_preprocessed)

    return model


def load_weights(path):
    weights = {}
    with open(path, 'r') as f:
        for line in f:
            items = [item.strip() for item in line.split(',')]
            weights[items[0]] = float(items[1])
    return weights


def get_score_dict(file_name):
    filepath = os.path.join(os.getcwd(), 'data', 'weights', file_name)
    score_dict = load_weights(filepath)

    return score_dict


def calc_score(score_dict, query):
    score = 0
    for k, v in score_dict.items():
        if k in query:
            score += v

    return 1 / (1 + math.exp(-1 * score))


def main():
    retro_dict = get_score_dict('retro.txt')
    query = input('Enter your idea: ')
    retro_score = calc_score(retro_dict, query)
    print(retro_score)


if __name__ == '__main__':
    main()
