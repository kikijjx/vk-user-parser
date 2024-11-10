import requests
import json
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI()
VK_API_VERSION = "5.199"

def get_user_info(token, user_id):
    base_url = "https://api.vk.com/method/"
    
    user_info_url = f"{base_url}users.get"
    user_info_params = {
        "user_ids": user_id,
        "fields": "followers_count",
        "access_token": token,
        "v": VK_API_VERSION
    }
    user_info_response = requests.get(user_info_url, params=user_info_params)
    user_info = user_info_response.json().get("response", [{}])[0]
    print(user_info)
    followers_url = f"{base_url}users.getFollowers"
    followers_params = {
        "user_id": user_id,
        "count": 1000,
        "access_token": token,
        "v": VK_API_VERSION
    }
    followers_response = requests.get(followers_url, params=followers_params)
    followers = followers_response.json().get("response", {}).get("items", [])
    
    subscriptions_url = f"{base_url}users.getSubscriptions"
    subscriptions_params = {
        "user_id": user_id,
        "access_token": token,
        "v": VK_API_VERSION
    }
    subscriptions_response = requests.get(subscriptions_url, params=subscriptions_params)
    subscription_ids = subscriptions_response.json().get("response", {}).get("groups", {}).get("items", [])
    
    groups_url = f"{base_url}groups.getById"
    groups_params = {
        "group_ids": ','.join(map(str, subscription_ids)),
        "access_token": token,
        "v": VK_API_VERSION
    }
    groups_response = requests.get(groups_url, params=groups_params)
    subscription_groups = groups_response.json().get("response", [])

    return {
        "user_info": user_info,
        "followers": followers,
        "subscriptions": subscription_groups
    }


@app.get("/data")
def read_data(token: str = Query(..., description="VK API Token"), user_id: str = Query(..., description="User ID")):
    data = get_user_info(token, user_id)
    return JSONResponse(content=data)
