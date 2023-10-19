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
    def wrapper(url):
        """Wrapper function."""
        response = f(url)
        count_key = f'count:{url}'
        response_key = f'response:{url}'
        r = redis.Redis()
        if r.exists(response_key):
            return r.get(response_key).decode('utf-8')
        r.set(response_key, response, ex=10)
        r.incr(count_key)
        return response
    return wrapper


@count
def get_page(url: str) -> str:
    """Returns a request's response."""
    return requests.get(url).text
