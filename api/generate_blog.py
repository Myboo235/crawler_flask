import markovify
import requests
from bs4 import BeautifulSoup
import random
import re
from googlesearch import search   
from bing_image_urls import bing_image_urls

topics = ["Solar_System", "Astronaut", "Artificial_intelligence", "Space_suit", "Space_exploration", "Spacecraft","Space_vehicle","Starship"]
# Transformer huggingface

def get_url_by_keyword(keyword):
    query = keyword + " wiki"

    urls = []
    for j in search(query, num=4, stop=1, pause=1): 
        urls.append(j) 
    random.shuffle(urls)
    return urls

def scrape_text_and_images(urls):
    all_text = ""
    all_image_urls = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            paragraphs = soup.find_all('p')[:10]

            text = ' '.join([p.get_text() for p in paragraphs])
            text = re.sub(r'\[.*?\]', '', text)
            text = re.sub(r'\s+', ' ', text).strip()

            image_urls = [
                f"https:{img['src']}" 
                if not img['src'].startswith('http') 
                and "svg.png" 
                not in img['src'] else img['src'] 
                for img in soup.find_all('img', src=True)[:20]]

            all_text += text + " "
            all_image_urls.extend(image_urls)
        except Exception as e:
            pass
    return all_text.strip(), all_image_urls

def is_valid_image_url(image_url):
    try:
        response = requests.head(image_url)
        return response.status_code == 200
    except Exception as e:
        return False


def generate_text_with_data(text_data,):
    try:
        text_model = markovify.Text(text_data)

        generated_text = text_model.make_short_sentence(400)

        return generated_text
    except Exception as e:
        return None

# Function to generate a blog post
def generate_blog_post_crawl(keyword):
    urls = get_url_by_keyword(keyword=keyword)
    text_data, image_urls = scrape_text_and_images(urls)


    blog_content = []
    if text_data:
        word_count = 0
        while word_count < 500:
            paragraph = generate_text_with_data(text_data)
            if paragraph:
                  word_count += len(paragraph.split())
                  blog_content.append(paragraph)

        blog_content_joined = [' '.join(map(str, blog_content[i:i+10])) for i in range(0, len(blog_content), 10)]

        title = f"A topic about {keyword.capitalize()}"
        content = '\n'.join(blog_content_joined)
        valid_image_urls = [url for url in image_urls if is_valid_image_url(url)]

        return {"title_output": title, "content_output": content, "imgs": valid_image_urls[:5]}
    else:
        print("Failed to scrape text from the webpage.")


def generate_blog_post_transformers(keyword):
    from transformers import pipeline
    generator = pipeline('text-generation')


    title = f"{keyword.capitalize()}"

    def generate_data(context, length=20):
        output = generator(context, max_length=length, do_sample=True, temperature=0.9,num_return_sequences=4)
        return output[0]["generated_text"]

    def generate_outputs():
        output = generate_data(title, 300)
        sentences = output.split(".")
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

        if sentences[-1].endswith("."):
            sentences[-1] = sentences[-1][:-1]

        title_output = sentences[0]
        content_output = ". ".join(sentences)

        imgs = bing_image_urls(keyword, limit=4)

        return {"title_output": title_output, "content_output": content_output, "imgs" : imgs}

    result = generate_outputs()
    return result
