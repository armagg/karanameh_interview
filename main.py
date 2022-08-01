from src.controller import app
from decouple import config

if __name__ == '__main__':
    app.run(host=config("HOST"), port=config('PORT'))