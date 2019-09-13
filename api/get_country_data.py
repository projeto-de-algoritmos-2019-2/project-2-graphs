import requests

def get_country_data():
    json_data = requests.get("https://restcountries.eu/rest/v2/all")

    json_data = json_data.json()

    print(json_data)

    response = []

    for country in json_data:
        obj = {
            'name': country['name'],
            'abbreviation': country['currencies'][0]['code'],
            'symbol': country['currencies'][0]['symbol'],
            'flagURL': country['flag']
        }

        response.append(obj)

    return response