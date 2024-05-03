#!/usr/bin/env python3
""" SIMPLE PAGINATION """


def index_range(page: int, page_size: int) -> tuple:
    """ Returns a tuple with the start and the end index of a page """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
