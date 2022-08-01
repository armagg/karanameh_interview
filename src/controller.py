from distutils.command.config import config
from flask import Flask, request
from .views import create_new_link, get_link
app = Flask(__name__)

@app.route("/short-link", methods =['POST'])
def create_short_link():
    form = request.form
    if 'url' in form:
        url = form.get('url')
        if 'number_of_charecters' in form and form.get('number_of_charecters') < config('MAX_CHAR'):
            number_of_charecters = form.get('number_of_charecters')
        else:
            number_of_charecters = config('DEFAULT_CHAR_NUMBER')
        try:
            shortened = create_new_link(url, number_of_charecters)
            return {'shortened': shortened}, 200
        except:
            pass


@app.route("/<path>", methods = ['GET'])
def get_shortened_link(path):
    if path == 'short-link':
        return {'msg': 'this path is used'}, 401
    try: 
        get_link(path)
    except:
        pass
