#!/usr/bin/env python3
""" Task 11 
"""


def schools_by_topic(mongo_collection, topic):
    """
    Finds a list of school having a specific topic
    """
    return mongo_collection.find({'topics': topic})
