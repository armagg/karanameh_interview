from flask import Flask, request
from database import create_new_link
app = Flask(__name__)

@app.route("/short-link", methods =['POST'])
def create_short_link():
    url = request.form.get("url")
    shortened = create_new_link(url, 5)
    return {'shortened': shortened}, 200

@app.route("/{path}", methods = ['GET'])
def get_shortened_link():
    path = request.path
    print(path)
