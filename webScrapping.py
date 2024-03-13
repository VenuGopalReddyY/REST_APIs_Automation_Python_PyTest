import requests
from bs4 import BeautifulSoup

URL = "https://rahulshettyacademy.com/AutomationPractice/"
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())