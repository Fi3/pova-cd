"""
Stupida prova
"""

import time
import os

import redis
from flask import Flask


APP = Flask(__name__)
REDIS_PORT = os.environ['REDIS_PORT'] # 6379
REDIS_HOST = os.environ['REDIS_HOST'] # 'redis'
HOST = os.environ['HOST'] # '0.0.0.0'
CACHE = redis.Redis(host='redis', port=REDIS_PORT)


def get_hit_count():
    """
    Ancor piu stupida funzione
    """
    retries = 5
    while True:
        try:
            return CACHE.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@APP.route('/')
def hello():
    """
    Un' altra funzione idiota
    """
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    APP.run(host=HOST, debug=True)
