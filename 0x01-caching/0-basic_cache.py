#!/usr/bin/env python3
"""basic cache class"""

from .base import BaseCaching


class BasicCache(BaseCaching):
    def __init__(self):
        """class constructor"""
        super().__init__()

    def put(self, key, item):
        """adds item to the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data if exists else None"""
        try:
            return self.cache_data[key]
        except ValueError:
            return None
