from flask import Flask, render_template, request, url_for, redirect
from flask import jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson import json_util
import json
import requests
from bs4 import BeautifulSoup  as bs
from uuid import uuid1
from flask_cors import CORS 

# Flask
app = Flask(__name__)
cors = CORS(app)
# MongoDB
client = MongoClient("mongodb://root:root@mongo:27017/")
db = client['crawl']
collection = db['crawl_data']

@app.get('/health_check')
def index():
    return json.loads(json_util.dumps({"health_status":'oke',})),200

@app.route('/')
def get_data():
    data = collection.find().sort({"_id":-1}) 
    data_list = list(data)

    return json.loads(json_util.dumps(data_list)),200

@app.post('/create')
def insert_data():
    content = dict(request.json)

    result_id = collection.insert_one(content).inserted_id

    return json.loads(json_util.dumps({
        "status": "Success",
        "_id": result_id
    })), 200

@app.post('/update')
def update_data():
    content = dict(request.json)
    _id = content.get("_id","")
    content.pop("_id")

    result = collection.update_one({"_id": ObjectId(_id)}, {"$set": content})    
    return json.loads(json_util.dumps({
        "status": "Success",
        "update_count" : result.modified_count
    })), 200



@app.post('/delete')   
def delete():
    _id = request.json.get("_id") 
    result = collection.delete_one({"_id": ObjectId(_id)})
 
    return {
        "status": "success",
        "deleted_count" : result.deleted_count
    }, 200

@app.get('/<id>')
def get_data_by_id(id):
    result = collection.find_one({"_id": ObjectId(id)})
    return json.loads(json_util.dumps(result)),200







    

    

    
    