import requests

def get_request(url:str):
    return "test_response"
requests.get=get_request
data=requests.get("https://open.spotify.com/")
print(data)
