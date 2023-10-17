#!/usr/bin/env python3
"""Task 8 module
"""


def list_all(mongo_collection):
    """list_all function

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List: List of Documents
    """
    return mongo_collection.find()
