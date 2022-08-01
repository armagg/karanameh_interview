import hashlib
from .services import cache_is_exist, cache_set, cache_get, get_db
from .exceptions import NotUrlError, NotExistErorr
from decouple import config
from validators import url as url_validator
from pymongo.errors import DuplicateKeyError

def create_new_link(url: str, number_of_charecters: int):
    if url_validator(url):
        shortened = hashlib.sha256(url.encode()).hexdigest()[:number_of_charecters]
        collection = get_db(config('DATABASE_NAME')).get_collection('links')
        try:
            collection.insert_one({'url': url, 'shortened': shortened})
        except DuplicateKeyError:
            """if the url already exist in database we do nothing"""
        except Exception as e:
            raise e
        return shortened
    else:
        raise NotUrlError()

def get_link(shortened: str):
    if cache_is_exist(shortened):
        return cache_get(shortened)
    else:
        col = get_db(config('DATABASE_NAME')).get_collection('links')
        query = col.find_one({'shortened': shortened})
        if 'url' in query:
            link = query['url']
            cache_set(shortened, link, int(config('CACHE_TTL')))
            return link
        else: 
            raise NotExistErorr