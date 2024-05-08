#!/usr/bin/env python3
"""basic cache class"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """basic cache class"""

    def __init__(self):
        """class constructor"""
        super().__init__()

    def put(self, key, item):
        """adds item to the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data if exists else None"""
        return self.cache_data.get(key, None)
