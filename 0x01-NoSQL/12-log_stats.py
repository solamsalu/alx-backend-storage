#!/usr/bin/env python3
"""Task 12 module
"""
from pymongo import MongoClient
from pymongo import MongoClient


# Create a connection to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Connect to the 'logs' database
db = client['logs']

# Connect to the 'nginx' collection
collection = db['nginx']

# Get the total number of logs
total_logs = collection.count_documents({})

# Get the number of documents for each method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({"method": method}) for method in methods}

# Get the number of documents with method=GET and path=/status
get_status_count = collection.count_documents({"method": "GET", "path": "/status"})

# Display the statistics
print(f"{total_logs} logs")
print("Methods:")
for method, count in method_counts.items():
    print(f"\t{method}: {count}")
print(f"GET /status: {get_status_count}")
