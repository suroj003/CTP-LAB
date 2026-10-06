import requests
from bs4 import BeautifulSoup


class News:
    def __init__(self):
        self.url = "https://news.ycombinator.com"

    def get_news(self):
        response = requests.get(self.url)

        soup = BeautifulSoup(response.text, "html.parser")

        news = soup.select("span.titleline > a")

        for i, item in enumerate(news, 1):
            title = item.text
            link = item.get("href")

            print(i, ".", title)
            print("Link:", link)
            print()


obj = News()
obj.get_news()