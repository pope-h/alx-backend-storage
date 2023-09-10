#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''
from functools import wraps
from typing import Callable
import redis
import requests

redis_store = redis.Redis()


def data_cacher(method: Callable) -> Callable:
    '''Caches the output of fetched data.
    '''
    @wraps(method)
    def invoker(url) -> str:
        '''The wrapper function for caching the output.
        '''
        # Incrementing count and getting count value
        count_key = f'count:{url}'
        redis_store.incr(count_key)
        count_value = redis_store.get(count_key).decode('utf-8')

        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')

        result = method(url)

        # Set count value to 0 if it's the first access
        if count_value == '1':
            redis_store.set(count_key, 0)

        # Cache the result for 10 seconds
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker

@data_cacher
def get_page(url: str) -> str:
    '''Returns the content of a URL after caching the request's response,
    and tracking the request.
    '''
    return requests.get(url).text
