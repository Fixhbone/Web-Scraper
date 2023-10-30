from bs4 import BeautifulSoup
import requests

def web_scraper(Base_Url=None):
    All_Quotes = []

    if Base_Url is None:
        Base_Url = input("Please enter the base URL: ")
    
    # Ensure the URL starts with https://
    if not Base_Url.startswith("http://") and not Base_Url.startswith("https://"):
        Base_Url = "https://" + Base_Url

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

    return All_Quotes

if __name__ == "__main__":
    # Test with a specific URL
    test_url = "https://quotes.toscrape.com/"
    scraper = web_scraper(test_url)
    print(scraper)





