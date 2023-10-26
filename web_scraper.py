from bs4 import BeautifulSoup
import requests

All_Quotes = []
Base_Url = "https://quotes.toscrape.com/"
url = "/page/1/"

while url:
    r = requests.get(f"{Base_Url}{url}")
    soup = BeautifulSoup(r.text, "html.parser")
    quotes = soup.find_all(class_="quote")

    for quote in quotes:
        All_Quotes.append({
            "text":   quote.find(class_="text").get_text(),
            "Author": quote.find(class_="author").get_text(),
            "URL": quote.find("a").get("href")
        })

    next_btn = soup.find(class_="next")
    url = next_btn.find("a")["href"] if next_btn else None

print(All_Quotes)
