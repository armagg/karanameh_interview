from src.controller import app
from decouple import config
from scripts.database_migrations import *


if __name__ == '__main__':
    app.run(host=config("HOST"), port=config('PORT'))
