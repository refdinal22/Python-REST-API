from flask import Flask
from flask_restful import Api

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__, static_folder='uploads')
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024