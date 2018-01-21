# run using:
#
# export FLASK_APP=server.py
# export FLASK_DEBUG=1
# flask run
#
# run publicly flask run --host=0.0.0.0
# export FLASK_APP=hello.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from scripts import test, model
import os
import json


app = Flask(__name__)
CORS(app)


print('{0}\n\tLoading Model ...\n{0}'.format('-' * 32))
model = model.main()
print('{0}\n\t\tSUCCESS!\n{0}'.format('-' * 32))


@app.route('/')
def index():
    return 'Index Page'


@app.route('/projects', methods=['GET', 'POST'])
def projects():

    project_description = request.args.get('project_description')

    print(request.method)
    if request.method == 'POST':
        data = 'DUMMY HAHAHAHAHA'

        # with open(fp, 'r') as f:
        #     data = json.load(f)

        dummy = {
            'projects': [
                {
                    'project_name': 'Trash Dummy haha',
                    'photo_url': '',
                    'tagline': 'asdjasd',
                    'project_url': 'http://asdjkla.penn.de/asjiod',
                    'tags': ['tag1', 'tag2'],
                    'similarity': 0.4
                },
                {
                    'project_name': 'Trash Dummy haha',
                    'photo_url': '',
                    'tagline': 'asdjasd',
                    'project_url': 'http://asdjkla.penn.de/asjiod',
                    'tags': ['tag1', 'fancytag2'],
                    'similarity': 0.3
                }
            ],
            'originality_score': 40
        }

        return jsonify(dummy)
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


print(model.calc_similarity(input('TYPE INPUT: ')))
