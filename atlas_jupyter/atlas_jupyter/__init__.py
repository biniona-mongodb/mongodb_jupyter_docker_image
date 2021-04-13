import os
import pymongo
import json

client = pymongo.MongoClient(os.getenv("CONNECTION_URI"))
db_str = os.getenv("DATABASE")
# hardcoded name of notebooks collection
notebook_col_str = "notebooks"
db = client[db_str]
notebook_col = db[notebook_col_str]
col = None

def set_col(new_col_str):
    col_str = new_col_str
    global col
    col = db[col_str]
