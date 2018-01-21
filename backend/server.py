# run using:
#
# export FLASK_APP=server.py
# export FLASK_DEBUG=1
# flask run
#
# run publicly flask run --host=0.0.0.0
# export FLASK_APP=server.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from scripts import test, model
import os
import json


app = Flask(__name__)
CORS(app)


print('{0}\n\tLoading Model ...\n{0}'.format('-' * 32))
sim_model = model.getModel()
print('{0}\n\t\tSUCCESS!\n{0}'.format('-' * 32))

retro_dict = model.get_score_dict('retro.txt')

tag_info = json.load(open('data/tagInfo.json'))


def format_response(predictions, originality_score=0, retro_score=0):
    result = {
        'projects': [],
        'originality_score': originality_score,
        'retro_score': retro_score,
        'tag_links': []
    }





    # dict_keys(
    #     ['class_name', 'comment_count', 'description', 'has_video', 'like_count', 'members', 'name', 'photo', 'slug',
    #      'tagline', 'tags', 'url', 'winner'])

    appended_tags = []

    for pred, score in predictions:
        tag_links = []
        if pred['tags']:
            for tag in pred['tags']:
                if tag.lower() in tag_info and tag.lower not in appended_tags:
                    tag_links.append(tag_info[tag.lower()])
                    appended_tags.append(tag.lower())

        result['tag_links'] = tag_links

        project = {
            'project_name': pred['name'],
            'photo_url': pred['photo'],
            'tagline': ' '.join(pred['tagline']),
            'project_url': pred['url'],
            'tags': pred['tags'],
            'winner': pred['winner'],
            'similarity': str(score)
        }

        result['projects'].append(project)


    return result


@app.route('/')
def index():
    return 'Index Page'


@app.route('/projects', methods=['POST'])
def projects():
    project_description = request.args.get('project_description')

    print(request.method)
    if request.method == 'POST':
        global sim_model
        # data = 'DUMMY HAHAHAHAHA'
        #
        # dummy = {
        #     'projects': [
        #         {
        #             'project_name': 'Trash Dummy haha',
        #             'photo_url': '',
        #             'tagline': 'asdjasd',
        #             'project_url': 'http://asdjkla.penn.de/asjiod',
        #             'tags': ['tag1', 'tag2'],
        #             'similarity': 0.4
        #         },
        #         {
        #             'project_name': 'Trash Dummy haha',
        #             'photo_url': '',
        #             'tagline': 'asdjasd',
        #             'project_url': 'http://asdjkla.penn.de/asjiod',
        #             'tags': ['tag1', 'fancytag2'],
        #             'similarity': 0.3
        #         }
        #     ],
        #     'originality_score': 40
        # }

        predictions, originality = sim_model.calc_similarity(project_description)
        # originality_score = model.get_originality_score()
        retro_score = model.calc_score(retro_dict, project_description)

        return jsonify(format_response(predictions, originality_score=originality, retro_score=retro_score))
    else:
        return 'get projects {}'.format(project_description)

    # if request.method == 'POST':
    #   query = 'sample idea query'

    #   top_pred = model.calc_similarity(query)

    #   result = {
    #       'projects':[],
    #       'originality_score': 0
    #       }
    #   for index, score in top_pred:
    #       temp = model.data[index]
    #       temp['similarity'] = score
    #       results['projects'].append(temp)
    #       results['originality_score'] += score
    #   results['originality'] /= len(top_pred)


# query = input('Enter your idea: ')
# print(sim_model.calc_similarity(query))
# print(model.calc_score(retro_dict, query))
