#!/usr/bin/env python3
""" Provides stats about Nginx logs restored in mongoDB """
import pymongo as pm
db = pm.MongoClient()
mydb = db["logs"]
mycol = mydb["nginx"]


if __name__ == "__main__":
    get_get = mycol.count_documents({"method": "GET"})
    get_post = mycol.count_documents({"method": "POST"})
    get_put = mycol.count_documents({"method": "PUT"})
    get_patch = mycol.count_documents({"method": "PATCH"})
    get_delete = mycol.count_documents({"method": "DELETE"})
    get_total = mycol.count_documents({})
    get_status = mycol.count_documents({"method": "GET", "path": "/status"})

    IPs = mycol.aggregate([{
        "$group": {
            "_id": "$ip", "count": {"$sum": 1}
            }}, {"$sort": {"count": -1}}, {"$limit": 10}, {"$project": {
                "_id": 0, "ip": "$_id", "count": 1}}
    ])

    print("{} logs".format(get_total))
    print("Methods:\n" +
          "\tmethod GET: {}\n".format(get_get) +
          "\tmethod POST: {}\n".format(get_post) +
          "\tmethod PUT: {}\n".format(get_put) +
          "\tmethod PATCH: {}\n".format(get_patch) +
          "\tmethod DELETE: {}".format(get_delete))
    print("{} status check".format(get_status))
    print("IPs:")
    for top in IPs:
        count = top.get("count")
        ip_address = top.get("ip")
        print("\t{}: {}".format(ip_address, count))
