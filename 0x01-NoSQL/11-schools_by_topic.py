#!/usr/bin/env python3
"""
11-schools_by_topic module
"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    specific_topic = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(specific_topic)]
