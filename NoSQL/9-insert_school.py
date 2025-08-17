#!/usr/bin/env python3
""" Function that inserts a new document """

import pymongo


def  insert_school(mongo_collection, **kwargs):
    """
    inserts a new document based on kwargs

    Args:
        mongo_collection: pymongo collection object
        kwargs: key-value

    Returns:
        new _id
    """
    res = mongo_collection.insert_one(kwargs)
    return res.insert_id
