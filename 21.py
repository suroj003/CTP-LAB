import requests
from bs4 import BeautifulSoup
import csv


class Books:
    def __init__(self):
        self.url = "https://books.toscrape.com/"

    def scrape(self):
        response = requests.get(self.url)

        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.select("article.product_pod")

        file = open("books.csv", "w", newline="", encoding="utf-8")

        writer = csv.writer(file)

        writer.writerow(["Book Name", "Price", "Availability"])

        for book in books:
            name = book.h3.a.get("title")
            price = book.select_one(".price_color").text
            stock = book.select_one(".availability").text.strip()

            writer.writerow([name, price, stock])

        file.close()

        print("Book data saved in books.csv")


obj = Books()
obj.scrape()