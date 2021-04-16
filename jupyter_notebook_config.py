import os
import pymongo
import json
import atlas_jupyter as a

#populate the file system on start with contents of mongocollection
for document in a.notebook_col.find():
    file_name = document["_id"]
    with open(file_name, 'w') as fp:
        json.dump(document["notebook"]["content"], fp, indent = 1)
    if document["notebook"].get("history"):
        with open(document["notebook"]["history"]["path"], 'w') as hfp:
            json.dump(document["notebook"]["history"]["history"], hfp, indent = 1)

def save_to_mongo (model, **kwargs):
    file_name, extension = os.path.splitext(kwargs["path"])
    if extension == ".ipyhistory":
        file_name = file_name.replace("/", "")
        filter_ = {"_id" : file_name+".ipynb"}
        update = {"$set" : {"notebook.history" : {"history" : model, "path" : kwargs["path"]}}}
        a.notebook_col.update_one(filter=filter_, update=update)
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
    a.notebook_col.replace_one(filter = id_dict, replacement = mongo_model, upsert = True)

c.FileContentsManager.pre_save_hook = save_to_mongo

c.NotebookApp.ip = 'localhost'
c.NotebookApp.port = 8888

c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy':
        "frame-ancestors http://localhost:8080 'self'"
    }
}
