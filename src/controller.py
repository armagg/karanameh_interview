from decouple import config
from flask import Flask, redirect, request
from .views import create_new_link, get_link
from .exceptions import NotUrlError, NotExistErorr
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
            shortened = create_new_link(url, int(number_of_charecters))
            return {'shortened': shortened}, 200
        except NotUrlError:
            return {'message': 'your url is not valid'}, 401
        except Exception as e:
            print(e)
            return {'message': 'some erorr happened!'}, 500


@app.route("/<path>", methods = ['GET'])
def get_shortened_link(path):
    if path == 'short-link':
        return {'msg': 'this path is used'}, 401
    try: 
        url = get_link(path)
        return {'url': url}, 200
    except NotExistErorr:
        return {'message': 'this path does not exist'}, 404 
    except Exception as e:
        print(e)
        return {'message': 'some erorr happened!'}, 500
