import requests
from bs4 import BeautifulSoup


def scrape_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract all headlines from the website - assuming they are in <h2> tags
    articles = soup.find_all("article")

    for idx, article in enumerate(articles, 1):
        heading_tag = article.find("h2")
        heading = heading_tag.text.strip() if heading_tag else "No heading"

        summary_tag = article.find("p")
        summary = summary_tag.text.strip() if summary_tag else "No summary"

        print(f"{idx}: Heading: {heading}\nSummary: {summary}\n")


scrape_headlines("https://www.indiatoday.in/headlines-today-top-stories")
