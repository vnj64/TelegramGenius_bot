import json
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from config import *



# Scally Milano albums
def albums_milano():
    url = "https://genius-song-lyrics1.p.rapidapi.com/artists/2040265/albums"

    querystring = {"per_page":"20","page":"1"}

    headers = {
        "X-RapidAPI-Key": "d8a2b24394msh530522f623e5ebcp1dff13jsn3401538088fc",
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


# Scally Milano songs
def songs_milano():
    url = "https://genius-song-lyrics1.p.rapidapi.com/artists/2040265/songs"

    querystring = {"sort":"title","per_page":"20","page":"1"}

    headers = {
        "X-RapidAPI-Key": "d8a2b24394msh530522f623e5ebcp1dff13jsn3401538088fc",
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    jsonData = response.json()['response']

    for data in jsonData['songs']:
        print('genius.com' + data['api_path'])
        


# Get top chart of genius.com
def top_chart():
    url = "https://genius-song-lyrics1.p.rapidapi.com/songs/chart"

    querystring = {"time_period":"day","chart_genre":"all","per_page":"10","page":"1"}

    headers = {
        "X-RapidAPI-Key": "c30a3e4eefmsh005fbb18a21016ap15e87cjsnac664dd22942",
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def new_func():
    url = "https://genius-song-lyrics1.p.rapidapi.com/search"

    querystring = {"q":"Scally Milano","per_page":"10","page":"1"}

    headers = {
        "X-RapidAPI-Key": "c30a3e4eefmsh005fbb18a21016ap15e87cjsnac664dd22942",
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


def artists_chart():

    url = "https://genius-song-lyrics1.p.rapidapi.com/artists/chart"

    querystring = {"time_period":"day","per_page":"10","page":"1"}

    headers = {
        "X-RapidAPI-Key": "c30a3e4eefmsh005fbb18a21016ap15e87cjsnac664dd22942",
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    jsonData = response.json()['response']
	
    for data in jsonData['chart_items']:
        print(data['item']['name'])


def take_lyrics():
    url = "https://genius-song-lyrics1.p.rapidapi.com/songs/6329375/lyrics"

    headers = {
        "X-RapidAPI-Key": "c30a3e4eefmsh005fbb18a21016ap15e87cjsnac664dd22942",
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    result = []
    
    jsonData = response.json()['response']
    double = jsonData['lyrics']
    bd = double
    result = bd['lyrics']['body']
    print(result['html'])