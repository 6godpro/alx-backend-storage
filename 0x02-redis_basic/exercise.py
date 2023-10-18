#!/usr/bin/env python3
"""
   This module contains a Cache class.
"""
import redis
from uuid import uuid4
from typing import Any, Callable, Union


class Cache:
    """Represents a Cache object."""
    def __init__(self) -> None:
        """Instantiates a Cache object."""
        self._redis = redis.Redis()
        self._redis.flushdb()

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
