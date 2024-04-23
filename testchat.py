import random
import gradio as gr
import json


data = json.load(open("questions_and_answers.json"))
print(type(data))

def response(message, history):
    if message == "":
        return "Please input your question"
    random.shuffle(data)
    for item in data:
        if message.lower() == item['Question'].lower():
            return "Answer: " + ' ' + item['Answer']
        if message.lower() in item['Question'].lower() or\
           message.lower() in item['Answer'].lower():
            return "Suggest question: "+item['Question'] +"\n" +\
                   "Answer          : " + ' ' + item['Answer']
        

    return "I don't know the answer to that question."

gr.ChatInterface(response).launch()