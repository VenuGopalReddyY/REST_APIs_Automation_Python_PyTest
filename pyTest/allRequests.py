import requests
import configparser
from utils.properitesRead import *
from utils.readEndpoints import *

URL = readProperitesFile()["API"]["endpoint"] + ReadEndpoints.GetBook
print(URL)
getResponse = requests.get(URL, params={"AuthorName":"Venu"})
# print(getResponse.text)
assert getResponse.status_code == 200
#print(getResponse.headers)
getResponse = getResponse.json()

for book in getResponse:
    print(book)

# print(getResponse)

book_id = getResponse[0]["isbn"]

# deleteBook = requests.delete(URL, json={"id":book_id})
json={"id":book_id}
print(json)