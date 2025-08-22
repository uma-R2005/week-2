import requests
from bs4 import BeautifulSoup

cities = ["mumbai", "delhi", "bangalore", "chennai", "kolkata"]

for city in cities:
    url = f"https://www.timeanddate.com/weather/india/{city}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract temperature and description
    temp = soup.find("div", class_="h2").text
    desc = soup.find("p").text

    print(f"Weather in {city.title()}: {desc}, {temp}")
