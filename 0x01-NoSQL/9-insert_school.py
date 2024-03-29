#!/usr/bin/env python3
""" Task 9 module
"""


def insert_school(mongo_collection, **kwargs):
    """insert_school function

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List: new _id
    """
    return mongo_collection.insert_one(kwargs).inserted_id
