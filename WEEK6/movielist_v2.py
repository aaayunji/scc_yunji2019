import requests as rq
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/running/current.nhn#'

res = rq.get(url)
soup = BeautifulSoup(res.content,'lxml')

Title_infos = soup.select('#content > div.article > div.lst_wrap > ul > dl > dt > a')

for info in Title_infos :

    Titles = info.select('.tit')

    for Title in Titles :
        print(Title.text)

movie_infos = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap')

for info in movie_infos :
    movies = info.select('.link_txt')
    for movie in movies :
        print(movie.text)
