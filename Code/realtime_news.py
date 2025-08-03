import requests
import csv
from datetime import datetime, timedelta

# Get yesterday's date in 'YYYY-MM-DD' format. You can change the range by modifying days=1.
lastest_day = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

# q: query keyword (e.g., 'AI', can be changed to other topics like 'crypto', 'sports', etc.)
url = ('https://newsapi.org/v2/everything?'
       'q=AI&'
       f'from={lastest_day}&'
       'sortBy=popularity&'
       'apiKey=6dada79f6f784ee4b908555069973c45')

response = requests.get(url)
data = response.json()
articles = data.get("articles", [])

with open("../dataset/latest_news.csv", mode="w", encoding="utf-8", newline="") as file:
       writer = csv.writer(file)
       writer.writerow(['source', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', 'content'])

       for article in articles:
              writer.writerow([
                     article.get('source', {}).get('name',''),
                     article.get('author', ''),
                     article.get('title', ''),
                     article.get('description', ''),
                     article.get('url', ''),
                     article.get('urlToImage', ''),
                     article.get('publishedAt', ''),
                     article.get('content', '')
              ])