from flask import Flask, render_template, request, url_for, redirect
from flask import jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson import json_util
import json
import requests
from bs4 import BeautifulSoup  as bs
from uuid import uuid1

app = Flask(__name__)

client = MongoClient("mongodb://root:root@mongo:27017/")

db = client['crawl']
collection = db['crawl_data']
url = "https://spaceandbeyondbox.com/the-space-and-beyond-blog/"
soup = bs(requests.get(url).content, "html.parser")


def clean_text(texts):
    for i in range(len(texts)):
        texts[i] = texts[i].text.strip()
    return texts
   
   
def get_data(url):
     
    subpage_soup = bs(requests.get(url).content, "html.parser")
    subpage_content = clean_text(subpage_soup.find("div", class_="entry-content").find_all("p"))
    subpage_title = subpage_soup.find("div", class_="entry-content").find("h1").text.strip()
    subpage_img = subpage_soup.find("span", class_="et_pb_image_wrap").find("img")["src"]
    
    return subpage_title, subpage_img, subpage_content


@app.get('/')
def index():
    return json.loads(json_util.dumps({"health_status":'oke',})),200


@app.route('/crawl')
def crawl():
    cnt = db['crawl_data'].count_documents({})
    if cnt > 0:
        return json.loads(json_util.dumps({"status":'success',"cnt":cnt})),200
    try:
        articles = []
        for article in soup.find_all("article"):
            # img = article.find("img")["src"]
            # title = article.find("h2").text
            # content = article.find("p").text
            subpage = article.find("a")["href"]
        
            data = get_data(subpage)
        

            articles.append({
                # "title": title,
                # "img": img,
                # "content": content,
                # "subpage": {
                    "title": data[0],
                    "img": data[1],
                    "content": data[2]
                # }
            })
        


       
        collection.insert_many(articles)

        cnt = collection.count_documents({})
        return json.loads(json_util.dumps({"status":'success',"cnt":cnt})),200
    except Exception as e:
        print(e)
        return json.loads(json_util.dumps({"status":'failed'})),500
    
@app.route('/crawl_data')
def crawl_data():
    data = collection.find() 
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
    data = collection.find_one({"_id": ObjectId(id)})
    return json.loads(json_util.dumps(data)),200







    

    

    
    