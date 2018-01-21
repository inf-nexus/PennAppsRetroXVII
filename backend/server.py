# run using: export FLASK_APP=server.py, flask run
# run publicly flask run --host=0.0.0.0
# export FLASK_APP=hello.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from scripts import test
import os
import json

app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
	return 'Index Page'

@app.route('/projects', methods=['GET', 'POST'])
def projects():
	fp = os.path.join(os.getcwd(), 'data-1.json')
	project_description = request.args.get('project_description')
	test.test()
	if request.method == 'POST':
		#return 'post projects {}'.format(project_description)
		#return app.send_static_file('data1.json')
		data = ''
		with open(fp, 'r') as f:
			data = json.load(f)
		print data
		return jsonify(data)
	else:
		return 'get projects {}'.format(project_description)