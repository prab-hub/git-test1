import requests, os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

base_url = "https://server.smartlead.ai/api/v1/campaigns/"
headers = {"accept": "application/json"}
params = {
    'api_key':api_key
}
response = requests.get(base_url, headers=headers, params=params)
print(response)