from src.services import get_db
from decouple import config

def create_unique_index_for_links():
    db = get_db(config('DATABASE_NAME'))
    col = db.get_collection('links')
    col.create_index([('url', 1)], unique=True)
    col.create_index([('shortened', 1)], unique=True)