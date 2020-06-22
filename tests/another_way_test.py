from flask import Flask
from flask_minio import Minio

minio = Minio()

app = Flask(__name__)

with app.app_context():
    minio.init_app(app)
    minio.connection.make_bucket('hello')