import json
import requests
from bs4 import BeautifulSoup as bs
from pymongo import MongoClient

client = MongoClient("mongodb://root:root@mongo:27017/")
db = client['crawl']
collection = db['crawl_data']

urls = [
    "https://spaceandbeyondbox.com/tour-the-inner-solar-system/",
    "https://spaceandbeyondbox.com/60-years-ago-alan-shepard-flew-to-space/",
    "https://spaceandbeyondbox.com/going-to-the-bathroom-in-outer-space/",
    "https://spaceandbeyondbox.com/is-exploring-space-hazardous-to-our-health/",
    "https://spaceandbeyondbox.com/who-has-the-right-of-way-in-space/",
    "https://spaceandbeyondbox.com/9-unusual-things-researchers-launched-into-space-for-science/",
    "https://spaceandbeyondbox.com/jupiters-most-interesting-moons/",
    "https://spaceandbeyondbox.com/four-things-you-probably-didnt-know-about-space/",
    "https://spaceandbeyondbox.com/the-benefits-of-space-exploration/",
    "https://spaceandbeyondbox.com/hazards-to-human-spaceflight/",
    "https://spaceandbeyondbox.com/explore-the-space-exploration-collection/",
    "https://spaceandbeyondbox.com/nasas-logo-from-meatball-to-worm-and-back/",
    "https://spaceandbeyondbox.com/dwarf-galaxies-in-the-local-group-and-beyond/",
    "https://spaceandbeyondbox.com/five-facts-you-probably-didnt-know-about-nasa/",
    "https://spaceandbeyondbox.com/forecasting-weather-on-the-sun/",
]
articles = []
print("""
============================
        CRAWL DATA...
============================""")
for url in urls:
    print(url)
    soup = bs(requests.get(url).content, "html.parser")

    title = soup.find(class_="et_pb_text_inner").find("strong").text.strip() if soup.find(class_="et_pb_text_inner").find("strong") else "no_title"
    content = []
    imgs = []


    image_wraps = soup.find_all(class_="et_pb_image_wrap")
    for i in image_wraps:
        if i.find("img"):
            imgs.append(i.find("img")["src"])

    content_wraps = soup.find_all(class_="et_pb_text_inner")
    for i in content_wraps:
        if i.find_all("p"):
            for p in i.find_all("p"):
                content.append(p.string)
    
    articles.append(
        {
            "title": title,
            "img": imgs,
            "content": content
        })

collection.insert_many(articles)
print("""
============================
          FINISH.
============================
""")