from flask import Flask, render_template, request, url_for, redirect
from flask import jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson import json_util
import json
import requests
from bs4 import BeautifulSoup
from uuid import uuid1

app = Flask(__name__)

client = MongoClient("mongodb://root:root@mongo:27017/")

db = client['crawl']
collection = db['crawl_data']

@app.get('/')
def index():
    return json.loads(json_util.dumps({"health_status":'oke',})),200


@app.route('/crawl')
def crawl():
    cnt = db['crawl_data'].count_documents({})
    if cnt > 0:
        return json.loads(json_util.dumps({"status":'success',"cnt":cnt})),200
    try:
        url = "https://www.trivianerd.com/topic/solar-system-trivia#sun-trivia"
        response = requests.get(url)
        html_content = response.text


        soup = BeautifulSoup(html_content, 'html.parser')

        question_elements = soup.find_all("p", class_="font-bold")
        questions = [question.text.replace("Question: ", "") for question in question_elements]

        answer_elements = soup.find_all("p", {":class":"(blur && globalBlur) && 'blur-sm'"})
        answers = [answer.text.replace("Answer: ", "") for answer in answer_elements]

        topics = soup.find_all("h2", class_="text-xl font-bold")
        tests = soup.find_all("div", class_ = "px-4 py-2 space-y-1")

        topic_counts = {}

        for topic, test in zip(topics, tests):
            topic_name = topic.text
            question_count = len(test.find_all("p", class_="font-bold"))
            topic_counts[topic_name] = question_count

        topic_elements = []
        for i in range(len(topics)):
            for _ in range(topic_counts[topics[i].text]):
                topic_elements.append(topics[i].text)

        qa_pairs = [{"question": question, "answer": answer, "topic": topic} for question, answer, topic in zip(questions, answers, topic_elements)]
        collection.insert_many(qa_pairs)

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








    

    

    
    