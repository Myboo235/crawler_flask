from flask import Flask, render_template, request, url_for, redirect
from flask import jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
import requests
from bs4 import BeautifulSoup as bs
from uuid import uuid1
from bson import json_util

app = Flask(__name__)

client = MongoClient("mongodb://root:root@mongo:27017/")

db = client.flask_db
todos = db.todos

@app.route('/', methods=('GET', 'POST'))
def index():

    return crawl_data()


@app.route('/crawl')
def crawl():
    try:




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


        articles = []
        for article in soup.find_all("article"):
            img = article.find("img")["src"]
            title = article.find("h2").text
            content = article.find("p").text
            subpage = article.find("a")["href"]
        
            data = get_data(subpage)
        

            articles.append({
                "title": title,
                "img": img,
                "content": content,
                "subpage": {
                    "title": data[0],
                    "img": data[1],
                    "content": data[2]
                }
            })
            


            data = json.dumps(articles, default=json_util.default)
            db = client['crawl']  # replace with your database name
            collection = db['crawl_data']  # replace with your collection name

            collection.insert_many(data)

            return 'oke'
    except Exception as e:
        print(e)
    
@app.route('/crawl_data')
def crawl_data():
    
    db = client['crawl']
    collection = db['crawl_data']
    data = collection.find() 


    data_list = list(data)

    
    return json.dumps(data_list)

@app.post('/create')
def insert_data():
    db = client['crawl']
    collection = db['crawl_data']

    _id = str(uuid1().hex)


    content = dict(request.json)
    content.update({"_id": _id})

    result = collection.insert_one(content)
    if not result.inserted_id:
        return {"message": "Failed to insert data"}, 500
    
    return {
        "message": "Success",
        "data": {
            "_id": result.inserted_id
        }
    }, 200

@app.post('/update')
def update_data():
    db = client['crawl']
    collection = db['crawl_data']

    _id = request.json.get("id")

    content = dict(request.json)
    content.pop("id")

    result = collection.update_one({"_id": _id}, {"$set": content})
    if not result.modified_count:
        return {"message": "Failed to update data"}, 500
    
    return {
        "message": "Success"
    }, 200


@app.post('/delete')   
def delete():
    db = client['crawl']
    collection = db['crawl_data']
    _id = request.json.get("id")

 
    result = collection.delete_one({"_id": ObjectId(_id)})


    if not result.deleted_count:
        return {"message": "Failed to delete data"}, 500
    
    return {
        "message": "Success"
    }, 200








    

    

    
    