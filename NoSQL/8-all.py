#!/usr/bin/env python3
""" Function that lists all documents in a MongoDB collection """

import pymongo


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object

    Returns:
        A list of documents (dictionaries). Returns an empty list if no documents are found.
    """
    return list(mongo_collection.find())
