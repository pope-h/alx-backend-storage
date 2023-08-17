#!/usr/bin/env python3
''' A module for using the Redis NoSQL data storage.
'''

import redis
from typing import Union
import uuid


class Cache:
    '''Represents an object for storing data in a Redis data storage.
    '''
    def __init__(self) -> None:
        '''Initializes a Cache instance.'''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key
