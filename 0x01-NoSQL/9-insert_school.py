#!/usr/bin/env python3
""" Defines insert_school """


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection based on kwargs"""
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
