#!/usr/bin/env python3
""" Task 101 module
"""


def top_students(mongo_collection):
    """top_students function

    Args:
        mongo_collection: pymongo collection object

    Returns:
        list
    """
    return mongo_collection.aggregate(
        [
            {"$project": {"name": "$name", "averageScore": {"$avg": "$topics.score"}}},
            {"$sort": {"averageScore": -1}},
        ]
    )
