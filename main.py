import requests
from datetime import datetime
import os
import dotenv

dotenv.load_dotenv()

USERNAME=os.getenv("USER")
TOKEN=os.getenv("TOKEN")

pixela_endpoint="https://pixe.la/v1/users"

user_prams={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response=requests.post(url=pixela_endpoint,json=user_prams)
# print(response.text)

headers={
    "X-USER-TOKEN":TOKEN
}

graph_config={
    "id":"graph1",
    "name":"Coding graph",
    "unit":"sec",
    "type":"int",
    "color":"ajisai"
}

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

pixel_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today=datetime.now()



pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many seconds do you done code?")
}

# response=requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
# print(response.text)


update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
update_pixel_data={
    "quantity":"6960"
}

response=requests.put(url=update_endpoint,json=update_pixel_data,headers=headers)
print(response.text)


delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

# response=requests.delete(url=delete_endpoint,headers=headers)
# print(response.text)
