#!/usr/bin/env python3
""" Function returns the list of school having a specific topic """

import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    list all topics.

    Args:
        mongo_collection: pymongo collection object
        topics: list of topics

    Returns:
        list all topics.
    """
    return list(mongo_collection.find({"topics": topic}))
