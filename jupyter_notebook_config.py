import os
import pymongo
import json

client = pymongo.MongoClient(os.getenv("CONNECTION_URI"))
db_str = os.getenv("DATABASE")
# hardcoded name of notebooks collection
col_str = "notebooks"
db = client[db_str]
col = db[col_str]

#populate the file system on start with contents of mongocollection
for document in col.find():
    file_name = document["_id"]
    print(file_name) # iterate the cursor
    with open(file_name, 'w') as fp:
        json.dump(document["notebook"]["content"], fp, indent = 1)

def save_to_mongo (model, **kwargs):

    # only run on notebooks
    if model['type'] != 'notebook':
        return
    # only run on nbformat v4
    if model['content']['nbformat'] != 4:
        return

    # save model to a mongodb collection
    id_dict = {"_id": kwargs["path"]}
    mongo_model = {"notebook" : model}
    mongo_model.update(id_dict)
    col.replace_one(filter = id_dict, replacement = mongo_model, upsert = True)

c.FileContentsManager.pre_save_hook = save_to_mongo
