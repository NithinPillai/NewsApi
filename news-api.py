import json
from fastapi import FastAPI
import requests

app = FastAPI()
key = '3990fcc18f674c02b11160f335649c20'

query = 'apple'
url = 'https://newsapi.org/v2/everything?q=healthcare&apiKey=3990fcc18f674c02b11160f335649c20'

@app.get('/fetch-news')
async def get_articles():
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        with open("news_articles.json", "w") as file:
            json.dump(data, file)
    