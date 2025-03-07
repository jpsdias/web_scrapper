from bs4 import BeautifulSoup
import requests

def main():
    # URL of the page you want to scrape
    url = "https://quotes.toscrape.com/"

    # Send an HTTP request to the URL and get the page content
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all <span> elements with class="text"
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    # Iterate over the found elements and print the text inside each
    for quote in quotes:
        print(quote.get_text())

    for author in authors:
        print(author.get_text())

if __name__ == "__main__":
    main()