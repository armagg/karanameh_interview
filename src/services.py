from pymongo import MongoClient
from decouple import config
import redis
mongo_client = MongoClient(config('MONGO_URL'))
r = redis.Redis(host=config("REDIS_HOST"), port=config('REDIS_PORT'), db=0)

def get_db(db_name: str):
    return mongo_client.get_database(db_name)


def cache_set(key, value, ttl):
    r.set(key, value, ttl)

def cache_is_exist(key: str):
    return r.exists(key)

def cache_get(key):
    return r.get(key)
