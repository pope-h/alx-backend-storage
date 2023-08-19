#!/usr/bin/env python3
""" Defines schools_by_topic """


def schools_by_topic(mongo_collection, topic):
    """ Lists school having a specific topic """
    filter_query = {"topics": topic}
    school_with_topic = mongo_collection.find(filter_query)
    return list(school_with_topic)
