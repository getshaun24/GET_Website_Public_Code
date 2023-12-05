import os

import redis
from rq import Worker, Queue, Connection
import sys
sys.path.insert(0, '/home/reid/Documents/Code/get_site/GET_Flask/')


listen = ['default']

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

redis_conn = redis.Redis(
    host=os.getenv("REDIS_HOST", "127.0.0.1"),
    port=os.getenv("REDIS_PORT", "6379"),
    password=os.getenv("REDIS_PASSWORD", ""),
)

redis_queue = Queue(connection=redis_conn)

# conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(redis_conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
