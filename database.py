import hashlib
from pymongo import MongoClient

connection = MongoClient("mongodb://root:example@localhost:27017")

def create_new_link(url: str, number_of_charecters):
    shortened = hashlib.md5(url.encode()).hexdigest()
    collection = connection.get_database('link-shortener').get_collection('links')
    try:
        collection.insert_one({'url': url, 'shortened': shortened})
    except:
        pass
    return shortened

def get_link():
    pass
