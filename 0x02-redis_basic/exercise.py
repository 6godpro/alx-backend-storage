#!/usr/bin/env python3
"""
   This module contains a Cache class.
"""
from ast import Call
import redis
from functools import wraps
from typing import Any, Callable, Union
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """
       Keeps track of the number of times that a
       method decorated with this function is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function."""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Records the input and output data of a method."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        result = method(self, *args, **kwargs)
        input_key = f'{method.__qualname__}:inputs'
        output_key = f'{method.__qualname__}:outputs'
        self._redis.rpush(input_key, str(args))
        self._redis.rpush(output_key, result)
        return result
    return wrapper


def replay(method: Callable):
    """Displays the history of calls of a particular function"""
    r = redis.Redis()
    input_key = f'{method.__qualname__}:inputs'
    output_key = f'{method.__qualname__}:outputs'
    key = method.__qualname__

    count = r.get(key)
    if count:
        _count = count.decode('utf-8')
    else:
        _count = '0'
    print(f'{key} was called {_count} times:')
    inputs = r.lrange(input_key, 0, -1)
    outputs = r.lrange(output_key, 0, -1)
    for i, o in zip(inputs, outputs):
        print(f'{key}(*{i.decode("utf-8")}) -> {o.decode("utf-8")}')


class Cache:
    """Represents a Cache object."""
    def __init__(self) -> None:
        """Instantiates a Cache object."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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
