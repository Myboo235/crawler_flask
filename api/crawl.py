import json
import requests
from bs4 import BeautifulSoup

# Fetch the HTML content of the webpage
url = "https://www.trivianerd.com/topic/solar-system-trivia#sun-trivia"
response = requests.get(url)
html_content = response.text


soup = BeautifulSoup(html_content, 'html.parser')

question_elements = soup.find_all("p", class_="font-bold")
questions = [question.text for question in question_elements]

# Find all elements containing answers
answer_elements = soup.find_all("p", {":class":"(blur && globalBlur) && 'blur-sm'"})
answers = [answer.text for answer in answer_elements]

print(answers)
# print(questions)
