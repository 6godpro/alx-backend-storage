#!/usr/bin/env python3
"""
   This module contains a Cache class.
"""
import redis
from uuid import uuid4
from typing import Union


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
