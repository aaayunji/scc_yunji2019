import requests
from bs4 import BeautifulSoup

# mongoDB 세팅 부분
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/running/current.nhn#', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')


Titles = soup.find_all('#content > div.article')

for Title in Titles:
		# title 안에 a 가 있으면,
    if not Title.a == None:
				# a의 text를 찍어본다.

        title = soup.select_one('#content > div.article > div.lst_wrap > ul > dl > dt > a').text

        print (title)

        break


movies = soup.find_all('dl', 'info_txt1')

for movie in movies:
    # movie 안에 a 가 있으면,
    if not movie.a == None:
# a의 text를 찍어본다.

        genre = soup.select_one('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(1) > dl > dd:nth-child(3) > dl > dd:nth-child(2) > span > a').text
        director = soup.select_one('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(1) > dl > dd:nth-child(3) > dl > dd:nth-child(4) > span > a').text

        actor = soup.select_one('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(1) > dl > dd:nth-child(3) > dl > dd:nth-child(6) > span > a').text

        print (genre,director,actor)

        break



