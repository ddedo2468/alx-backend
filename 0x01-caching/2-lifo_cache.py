#!/usr/bin/env python3
"""simple lifo cache"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Basic LIFO cahe"""

    def __init__(self):
        """constructor method"""
        super().__init__()

    def put(self, key, item):
        """add items to cache dict"""
        if not (key and item):
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            keys = list(self.cache_data)

            del self.cache_data[keys[-1]]

            print(f"DISCARD: {keys[-1]}")

        self.cache_data[key] = item

    def get(self, key):
        """get an item from the cache"""
        return self.cache_data.get(key, None)
