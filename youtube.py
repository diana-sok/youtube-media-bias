import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb://localhost:27017/")  # conn to cluster
db = cluster["youtube"]  # create database named youtube
collection = db["youtube"]  # in db, create collection called youtube

# to check if database exists
db_list = cluster.list_database_names()
if "youtube" in db_list:
    print("The database exists.")

# check if collection exists
collection_list = db.list_collection_names()
if "customers" in collection_list:
    print("The collection exists.")