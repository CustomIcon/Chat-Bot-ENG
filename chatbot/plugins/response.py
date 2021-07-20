
from requests.exceptions import HTTPError
import requests

url = "https://api.affiliateplus.xyz/api"


def chatbot(msg, ainame, onwer, userid):
    base = f'{url}/chatbot?message={msg}&botname={ainame}&ownername={owner}&user={userid}'
    response = requests.get(base)
    response.raise_for_status()
    jsonResponse = response.json()
    message = (jsonResponse["message"])
    return message
