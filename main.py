import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# DRIVER = webdriver.Chrome(executable_path="/home/sirius/TelegramGenius/chromedriver/chromedriver")

# def genius_parse(url):

#     artist_name = 'OG BUDA'

#     if artist_name:
#         try:
#             DRIVER.get(url=url)
            
#             time.sleep(3)
            
#             search = DRIVER.find_element('xpath', '//*[@id="application"]/div/div[1]/div[1]/form/input')
#             search.click()
#             search.send_keys(f'{artist_name}')
            
#             search.send_keys(Keys.ENTER)

#             time.sleep(6)

#             # first_artist = DRIVER.find_element('xpath', '/html/body/div[1]/search-form/form/div[2]/div/search-results/div[2]/div/search-result-section[1]/div/div[2]/search-result-items/div/search-result-item/div/mini-artist-card/a/div[2]/div')

#             # first_artist.click()
        

#         except Exception as ex:
#             print(ex)

#         finally:
#             DRIVER.close()
#             DRIVER.quit()
#     else:
#         return "Введите имя артиста: "

# genius_parse('https://genius.com/')


# # Scally Milano albums
# def albums_milano():
#     url = "https://genius-song-lyrics1.p.rapidapi.com/artists/2040265/albums"

#     querystring = {"per_page":"20","page":"1"}

#     headers = {
#         "X-RapidAPI-Key": "d8a2b24394msh530522f623e5ebcp1dff13jsn3401538088fc",
#         "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
#     }

#     response = requests.request("GET", url, headers=headers, params=querystring)

#     print(response.text)


# # Scally Milano songs
# def songs_milano():
#     url = "https://genius-song-lyrics1.p.rapidapi.com/artists/2040265/songs"

#     querystring = {"sort":"title","per_page":"20","page":"1"}

#     headers = {
#         "X-RapidAPI-Key": "d8a2b24394msh530522f623e5ebcp1dff13jsn3401538088fc",
#         "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
#     }

#     response = requests.request("GET", url, headers=headers, params=querystring)

#     jsonData = response.json()['response']

#     for data in jsonData['songs']:
#         print('genius.com' + data['api_path'])
        

# # songs_milano()

# # Get top chart of genius.com
# def top_chart():
#     url = "https://genius-song-lyrics1.p.rapidapi.com/songs/chart"

#     querystring = {"time_period":"day","chart_genre":"all","per_page":"50","page":"1"}

#     headers = {
#         "X-RapidAPI-Key": "d8a2b24394msh530522f623e5ebcp1dff13jsn3401538088fc",
#         "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
#     }

#     response = requests.request("GET", url, headers=headers, params=querystring)

#     jsonData = response.json()
#     print(jsonData)

# # top_chart()

url = "https://genius-song-lyrics1.p.rapidapi.com/artists/chart"

querystring = {"time_period":"day","per_page":"10","page":"2"}

headers = {
	"X-RapidAPI-Key": "d8a2b24394msh530522f623e5ebcp1dff13jsn3401538088fc",
	"X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

jsonData = response.json()['response']
for data in jsonData['chart_items']:
    print(data['item'])