from flask import Flask, render_template, request, url_for, redirect
from flask import jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

client = MongoClient("mongodb://root:root@mongo:27017/")

db = client.flask_db
todos = db.todos

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))

    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)

@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))


@app.route('/crawl')
def crawl():
    try:
        url = "https://www.trivianerd.com/topic/solar-system-trivia#sun-trivia"
        response = requests.get(url)
        html_content = response.text


        soup = BeautifulSoup(html_content, 'html.parser')

        question_elements = soup.find_all("p", class_="font-bold")
        questions = [question.text.replace("Question: ", "") for question in question_elements]

        # Find all elements containing answers
        answer_elements = soup.find_all("p", {":class":"(blur && globalBlur) && 'blur-sm'"})
        answers = [answer.text.replace("Answer: ", "") for answer in answer_elements]

        # Create a list of dictionaries to store questions and answers
        # qa_pairs = [{"question": question, "answer": answer} for question, answer in zip(questions, answers)]


        topics = soup.find_all("h2", class_="text-xl font-bold")
        tests = soup.find_all("div", class_ = "px-4 py-2 space-y-1")

        topic_counts = {}

        for topic, test in zip(topics, tests):
            topic_name = topic.text
            question_count = len(test.find_all("p", class_="font-bold"))
            topic_counts[topic_name] = question_count


        sum = 0
        topic_elements = []
        for i in range(len(topics)):

            for j in range(topic_counts[topics[i].text]):
                # print("Topic: ", topics[i].text)
                topic_elements.append(topics[i].text)
                # print("Question: ", questions[j+sum])
                # print("Answer: ", answers[j+sum])
            sum += int(topic_counts[topics[i].text])

        qa_pairs = [{"id": i, "question": question, "answer": answer, "topic": topic} for i, (question, answer, topic) in enumerate(zip( questions, answers, topic_elements))]



        db = client['crawl']  # replace with your database name
        collection = db['crawl_data']  # replace with your collection name

        collection.insert_many(qa_pairs)

        return 'oke'
    except Exception as e:
        print(e)
    
@app.route('/crawl_data')
def crawl_data():
    
    db = client['crawl']
    collection = db['crawl_data']
    data = collection.find({}, {"_id": 0})  # Exclude _id

    # Convert the cursor object to a list
    data_list = list(data)

    # Convert the list to a JSON object and return it withou sorting the keys (default)
    return jsonify(data_list)