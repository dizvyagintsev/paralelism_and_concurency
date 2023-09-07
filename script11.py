import concurrent.futures
import threading
from collections import defaultdict
import time

import requests as requests

cache = {}
cache_locks = defaultdict(threading.Lock)


def thread_worker(url):
    print(f"Processing {url}")

    with cache_locks[url]:
        if url not in cache:
            print(f"Fetching {url}")
            cache[url] = requests.get(url).json()

    print(f"Processed {url}")
    return cache[url]


urls = [
    *["https://jsonplaceholder.typicode.com/todos/1"] * 3,
    *["https://jsonplaceholder.typicode.com/todos/2"] * 3,
    *["https://jsonplaceholder.typicode.com/todos/3"] * 3,
    *["https://jsonplaceholder.typicode.com/todos/4"] * 3,
    *["https://jsonplaceholder.typicode.com/todos/5"] * 3,
    *["https://jsonplaceholder.typicode.com/todos/6"] * 3,
    *["https://jsonplaceholder.typicode.com/todos/7"] * 3,
    *["https://jsonplaceholder.typicode.com/todos/8"] * 3,
    *["https://jsonplaceholder.typicode.com/todos/9"] * 3,
    *["https://jsonplaceholder.typicode.com/todos/10"] * 3,
]


start = time.time()
with concurrent.futures.ThreadPoolExecutor() as pool:
    results = pool.map(thread_worker, urls)
print(f"Elapsed time: {time.time() - start}")
