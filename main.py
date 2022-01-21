import requests
from bs4 import BeautifulSoup
import pprint

# Create a response object.
res = requests.get("https://news.ycombinator.com/news")

# Use BeautifulSoup to parse.
soup = BeautifulSoup(res.text, "html.parser")
news_link = soup.select(".titlelink")
subtext = soup.select(".subtext")

# Function to sort news by votes.
def sort_news_by_votes(hnlist):
  return sorted(hnlist, key= lambda k:k["votes"], reverse=True)

# Function to grab the title link and votes of each news on HN.
def custom_news_format(news_link, subtext):
  news = []
  for i, item in enumerate(news_link):
    title = item.getText()
    href = item.get("href", None)
    vote = subtext[i].select(".score")
    if len(vote):
      points = int(vote[0].getText().replace(" points", ""))
      if points > 99: # Search only for news with at least 100 points.
        news.append({"title": title, "href": href, "votes": points})
  return sort_news_by_votes(news)

pprint.pprint(custom_news_format(news_link, subtext))
