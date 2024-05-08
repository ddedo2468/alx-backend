#!/usr/bin/env python3
"""basic MRU cache class"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """simple mru cache class"""

    def __init__(self):
        """constructor method"""
        super().__init__()
        self.used_items = []

    def put(self, key, item):
        """adding items to the class"""
        if not (key and item):
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            removed = self.used_items.pop()
            self.cache_data.pop(removed)
            print("DISCARD: {}".format(removed))

        self.cache_data[key] = item
        self.used_items.append(key)

    def get(self, key):
        """get item from mru cache"""

        if key in self.cache_data:
            self.used_items.remove(key)
            self.used_items.append(key)

        return self.cache_data.get(key, None)
