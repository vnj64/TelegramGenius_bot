import requests



# Scally Milano albums
def albums_milano():
    url = "https://host/artists/2040265/albums"

    querystring = {"per_page":"20","page":"1"}

    headers = {
        "X-RapidAPI-Key": "api_key",
        "X-RapidAPI-Host": "host"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


# Scally Milano songs
def songs_milano():
    url = "https://host/artists/2040265/songs"

    querystring = {"sort":"title","per_page":"20","page":"1"}

    headers = {
        "X-RapidAPI-Key": "api_key",
        "X-RapidAPI-Host": "host"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    jsonData = response.json()['response']

    for data in jsonData['songs']:
        print('genius.com' + data['api_path'])
        


# Get top chart of genius.com
def top_chart():
    url = "https://host/songs/chart"

    querystring = {"time_period":"day","chart_genre":"all","per_page":"10","page":"1"}

    headers = {
        "X-RapidAPI-Key": "api_key",
        "X-RapidAPI-Host": "host"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def new_func():
    url = "https://host/search"

    querystring = {"q":"Scally Milano","per_page":"10","page":"1"}

    headers = {
        "X-RapidAPI-Key": "api_key",
        "X-RapidAPI-Host": "host"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def artists_chart():

    url = "https://host/artists/chart"

    querystring = {"time_period":"day","per_page":"10","page":"1"}

    headers = {
        "X-RapidAPI-Key": "api_key",
        "X-RapidAPI-Host": "host"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    jsonData = response.json()['response']
	
    for data in jsonData['chart_items']:
        print(data['item']['name'])


def take_lyrics():
    url = "https://host/songs/6329375/lyrics"

    headers = {
        "X-RapidAPI-Key": "api_key",
        "X-RapidAPI-Host": "host"
    }

    response = requests.request("GET", url, headers=headers)

    result = []
    
    jsonData = response.json()['response']
    double = jsonData['lyrics']
    bd = double
    result = bd['lyrics']['body']
    print(result['html'])