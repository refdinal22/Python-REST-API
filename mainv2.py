import os
import urllib.request
from app import app
from flask import Flask, request, redirect, jsonify, send_from_directory
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename

api = Api(app)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class Retrieval(Resource):	
	def post(self):
		if 'file' not in request.files:
			resp = jsonify({'message' : 'No file part in the request'})
			resp.status_code = 400
			return resp
		file = request.files['file']		

		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		resp = jsonify({'message' : 'File successfully uploaded'})
		resp.status_code = 201

		return resp

api.add_resource(Retrieval, '/retrieval/image', endpoint='image')

if __name__ == "__main__":
    app.run(debug=True)	