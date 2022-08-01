import hashlib
from .services import cache_is_exist, cache_set, cache_get, get_db
from decouple import config
def create_new_link(url: str, number_of_charecters):

    shortened = hashlib.md5(url.encode()).hexdigest()[:number_of_charecters]
    collection = get_db(config('DATABASE_NAME')).get_collection('links')
    try:
        collection.insert_one({'url': url, 'shortened': shortened})
    except:
        pass
    return shortened

def get_link():
    pass
