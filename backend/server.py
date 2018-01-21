# run using: export FLASK_APP=server.py, flask run
# run publicly flask run --host=0.0.0.0
# export FLASK_APP=hello.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from scripts import test, model
import os
import json

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/projects', methods=['POST'])
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
                    'photo_url': 'https://firefly-challengepost.netdna-ssl.com/usercontent/fill/333/222/cGhvdG9zL3Byb2R1Y3Rpb24vc29mdHdhcmVfdGh1bWJuYWlsX3Bob3Rvcy8wMDAvNTMyLzc0OS9kYXRhcy9vcmlnaW5hbC5wbmc=/Screen_Shot_2017-09-10_at_9.46.13_AM.png?signature=281fd2d2f8db7b19fcc81c7c1378cbf9de622059',
                    'tagline': 'asdjasd',
                    'project_url': 'https://devpost.com/software/sorty-mcsortface',
                    'tags': ['tag1', 'tag2'],
                    'similarity': 0.4
                },
                {
                    'project_name': 'Trash Dummy haha',
                    'photo_url': 'https://devpost-challengepost.netdna-ssl.com/assets/defaults/thumbnail-placeholder-42bcab8d8178b413922ae2877d8b0868.gif',
                    'tagline': 'asdjasd',
                    'project_url': 'https://devpost.com/software/pillar-egulwv',
                    'tags': ['tag1', 'fancytag2'],
                    'similarity': 0.3
                }
            ],
            'originality_score': 40,
            'tutorial': "Based on the information you provided we believe these sources will be helpful to create your idea.\n\
            github.com\n\
            khanacademy.org"
        }

        return jsonify(dummy)
    else:
        return 'get projects {}'.format(project_description)