#!/usr/bin/env python3
"""
In this tasks, we will implement a get_page function
(prototype: def get_page(url: str) -> str:).
The core of the function is very simple. It uses the
requests module to obtain the HTML content of a particular
URL and returns it.

Inside get_page track how many times a particular URL
was accessed in the key "count:{url}" and cache the
result with an expiration time of 10 seconds.

Tip: Use http://slowwly.robertomurray.co.uk to simulate
a slow response and test your caching.

Bonus: implement this use case with decorators.
"""
import redis
import requests
from functools import wraps


def count(f):
    """Tracks the number of times a url was accessed."""
    @wraps(f)
    def wrapper(*args, **kwargs):
        """Wrapper function."""
        key = f'count:{args[0]}'
        r = redis.Redis()
        if not r.exists(key):
            r.set(key, 0, ex=10)
        r.incr(key)
        return f(*args, **kwargs)
    return wrapper


@count
def get_page(url: str) -> str:
    """Returns a request's response."""
    return requests.get(url).text
