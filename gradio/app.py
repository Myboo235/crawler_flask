import requests, json
import gradio as gr
import bs4

model = 'tinyllama' 
context = [] 


topics = ["Solar System"]
url = 'https://en.wikipedia.org/wiki/Solar_System'

print("---get crawl data---")
response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'})
soup = bs4.BeautifulSoup(response.text, 'lxml')
paragraphs = soup.find_all('p')

topics_string = ' and '.join(topics[:-1]) + ' and ' + topics[-1]
text_crawled = ' '.join([p.get_text(strip=True) for p in paragraphs])

prompt = f"""
    You are a helpful assistant who provides detailed and accurate information.
    I have crawled a large amount of text from various sources, and I would like you to analyze the text and provide insights on the following topics: 
    {topics_string}. 
    Here is the text I have crawled: 
    ----
    {text_crawled}
    ----
    Please provide a detailed analysis of the topic, answer the question.
    """


is_reading = False

def generate(input, context):
    r = requests.post(f"http://ollama/api/generate",json={'model': model,'prompt': input})
    r.raise_for_status()
    response = ""  
    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get('response', '')
        if 'error' in body:
            raise Exception(body['error'])
        response += response_part
        if body.get('done', False):
            context = body.get('context', [])
            return response, context



def chat(input, chat_history):
    chat_history = chat_history or []
    global context
    output, context = generate(input, context)
    chat_history.append((input, output))
    return chat_history, chat_history

print("---Run gradio server---")

if not is_reading:
    generate(prompt,context)
block = gr.Blocks()
with block:
    gr.Markdown("""<h1><center> Jarvis </center></h1>""")
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder="Type here")
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chat, inputs=[message, state], outputs=[chatbot, state])


block.launch(server_name="0.0.0.0",debug=True)