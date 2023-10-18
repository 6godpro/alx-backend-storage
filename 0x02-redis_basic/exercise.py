#!/usr/bin/env python3
"""
   This module contains a Cache class.
"""
import redis
from functools import wraps
from typing import Any, Callable, Union
from uuid import uuid4


def count_calls(f: Callable) -> Callable:
    """
       Keeps track of the number of times that a
       method decorated with this function is called.
    """
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        """Wrapper function."""
        self._redis.incr(f.__qualname__)
        return f(self, *args, **kwargs)
    return wrapper


class Cache:
    """Represents a Cache object."""
    def __init__(self) -> None:
        """Instantiates a Cache object."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
           Stores data in the cache using a randomly
           generated string and returns the generated
           string.
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn=None) -> Any:
        """Returns the data associated with the key argument."""
        if self._redis.exists(key):
            if fn is not None:
                return fn(self._redis.get(key))
            return self._redis.get(key)
        return None

    def get_str(self, key: str) -> str:
        """Parameterizes the get method with a str type."""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Parameterizes the get method with an int type."""
        return self.get(key, int)
