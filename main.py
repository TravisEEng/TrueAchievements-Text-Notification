from bs4 import BeautifulSoup
import requests

url = "https://www.trueachievements.com/gamer/XxXxS8TNxXxX/achievements"
result = requests.get(url)

print(result.status_code)

#soup = BeautifulSoup(result.content)

#print(soup.prettify())
