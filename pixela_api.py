import requests
import datetime as dt

user_name = "yash6565df"
token = "reg46erg45e6rg"

pixela_endpoint = "https://pixe.la/v1/users"


# to create a account and setup:
# user_params = {
#   "token": token,
#   "username": user_name,
#   "agreeTermsOfService": "yes",
#   "notMinor": "yes",
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# graph_config = {
#   "id": "graph1",
#   "name": "Coding graph",
#   "unit": "Hr",
#   "type": "float",
#   "color": "ajisai"
# }

header = {
  "X-USER-TOKEN": token
}

today =dt.datetime.now()
today = today.strftime("%Y%m%d")
post_config = {
  "date": today,
  "quantity": input("How many hrs did you code today ???")
}

# to update a pixel
# update_config = {
#   "quantity": "6",
  
# }


response = requests.post(url=f"{pixela_endpoint}/{user_name}/graphs/graph1", json=post_config, headers=header)
print(response.text)


# for deleting a pixel
# DELETE = requests.delete(f"https://pixe.la/v1/users/{user_name}/graphs/graph1/{today}", headers=header)
# print(DELETE.text)

