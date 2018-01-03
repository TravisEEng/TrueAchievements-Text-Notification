from bs4 import BeautifulSoup
import requests

url = "https://www.trueachievements.com/"
content = requests.get(url)

print(content.status_code)

print("Hello World!")

#soup = BeautifulSoup(content)

#print(soup.prettify())
