#!/usr/bin/env python3
"""
8-all module
"""


def list_all(mongo_collections):
    """Return all documents in a collection"""

    return [doc for doc in mongo_collections.find()]
