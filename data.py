import requests

# https://opentdb.com
url = "https://opentdb.com/api.php"
params = {
    "amount": 10,
    "difficulty": "easy",
    "type": "boolean",
    "category": 12,  # 12 for music
}
response = requests.get(url=url, params=params)
response.raise_for_status()
question_data = response.json()['results']
