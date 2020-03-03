import requests, json

def fetch_data(location):
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key":"bd66f550fd3e4eb083c194114200203",
        "q":location   
    }

    response = requests.post(url, data=params)
    return json.loads(response.text)
