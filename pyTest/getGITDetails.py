import requests

# URL = "https://github.com"
#
# response = requests.get(URL, auth=('venumi3gopal@gmail.com', '5thAugust1998'))
# print(response.status_code)
# assert response.status_code == 200
#
#
# URL1 = "https://httpbin.org/post"
# with open("/Users/venu/Desktop/Workspace/BackendAutomation/pyTest/sampleFile.txt", "rb") as file:
#     response = requests.post(URL1, files={"file": file})
#     assert response.status_code == 200
#     print(response.status_code)

URL = "https://petstore.swagger.io/v2/pet/98/uploadImage"
with open("/Users/venu/Desktop/Workspace/BackendAutomation/pyTest/sampleFile.txt", "rb") as file:
    response = requests.post(URL, files={"file": file})
    print(response.status_code)
    print(response.text)
