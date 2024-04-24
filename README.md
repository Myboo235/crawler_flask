# CRAWLER (FLASK,MONGODB,MONGO_EXPRESS) & CHATBOT (GRADIO)
## Description
- This is a simple api for web crawler using flask, mongodb.
## Folder structure
```
    ├── api                     # API folder
    │    ├── app.py             # api file
    │    ├── template           # Template folder to show view
    │    ├── ...    
    ├── gradio                  # Chatbot folder
    │    ├── testchat.py        # testchat file
    │    ├── ...    
    ├── ...                    
    ├── Dockerfile                     
    ├── docker-compose.yml                    
    ├── requirements.txt        # Dependencies to run           
    ├── ...
    └── README.md
```
## How to run
###  *Make sure you have docker or you can run it in local
> Using docker 
Check docker 
```
docker --version
``` 
```
Docker version 26.0.1, build d260a54
```
Let's build
```
docker compose build
```
After that run compose
```docker
docker compose up
```
And Hola:
>API
![demo.png](./img/demo.png)

>CHATBOT
![chatbot.png](./img/chatbot.png)
---
> Using local
- You should have your mongo db run in local port 27017
```bash
pip install --no-cache-dir -r requirements.txt
```
Run app
```bash
cd api && flask run
```
Run chatbot
```bash
cd gradio && python testchat.py
```
### Access database 
> Using docker (only)
![demo.png](./img/database.png)
- or you can use [MongoDB Compass]("https://www.mongodb.com/products/tools/compass)
## That done!