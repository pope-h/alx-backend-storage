#!/usr/bin/env python3
""" Provides stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    logs_db = client.logs  # Access the "logs" database
    nginx_collection = logs_db.nginx
    # Access the "nginx" collection within the "logs" database

    total_logs = nginx_collection.count_documents({})
    # Total number of documents in the collection
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    status_check_count = nginx_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(status_check_count, "status check")
