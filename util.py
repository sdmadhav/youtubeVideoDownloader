
import requests
from bs4 import BeautifulSoup
from yt_dlp import YoutubeDL



def title(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html.parser')
    title = soup.find_all('meta', {'name': 'title'})
    # download(url)
    return (title[0]['content'])

def thumbnail(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html.parser')
    thumbnailUrl = soup.find_all('link', {'itemprop': 'thumbnailUrl'})
    # print(thumbnailUrl[0]['href'])
    # download(url)
    return (thumbnailUrl[0]['href'])

def keyword(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html.parser')
    keywords = soup.find_all('meta', {'name': 'keywords'})
    print(keywords[0]['content'])
    # download(url)
    return (keywords[0]['content'])

import time
def download(url):
    with YoutubeDL() as ydl:
        ydl.download([url])

if __name__ == '__main__':
    # load_saved_artifacts()
    # print(get_location_names())
    print(title('https://www.youtube.com/watch?v=7pYThX-aXLs'))
    # print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    # print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    # print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location