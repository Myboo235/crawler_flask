import json
import requests
from bs4 import BeautifulSoup

# Fetch the HTML content of the webpage
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
qa_pairs = [{"question": question, "answer": answer} for question, answer in zip(questions, answers)]

# Save the data as JSON
# with open("questions_and_answers.json", "w") as json_file:
#     json.dump(qa_pairs, json_file, indent=2)  # indent for pretty formatting



from pymongo import MongoClient

# Create a client connection to your MongoDB instance

client = MongoClient("mongodb://root:root@mongo:27017/")

# Connect to your database
db = client['crawl']  # replace with your database name

# Get your collection
collection = db['data_crawl']  # replace with your collection name

# Insert the data
collection.insert_many(qa_pairs)

# Close the connection
client.close()


