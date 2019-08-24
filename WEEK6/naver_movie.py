

#import
from bs4 import BeautifulSoup
from urllib.request import urlopen
#몽고DB연결

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


url = urlopen("https://movie.naver.com/movie/running/current.nhn")
bs = BeautifulSoup(url,'html.parser')
body = bs.body

target = body.find(class_="lst_detail_t1")
list = target.find_all('li')

no = 1
for n in range(0,len(list)) :
    print("==================================")
    print("No.",no)
    no += 1
    # 영화 제목
    title = list[n].find(class_="tit").find("a").text
    print("영화 제목 :\t",title)

    #감독
    try:
        director = list[n].find(class_="info_txt1").find_all("dd")[1].find("span").find_all("a")
        directorList = [director.text.strip() for director in director]
        print("제작 감독 :\t",directorList)
    except IndexError:
        print("제작 감독 :\t 정보 없음")
        directorList = "정보 없음"

    #출연 배우
    try:
        cast = list[n].find(class_="lst_dsc").find("dl", class_="info_txt1").find_all("dd")[2].find(class_="link_txt").find_all("a")
        castList = [cast.text.strip() for cast in cast]
        print("출연 배우 :\t",castList)
    except IndexError:
        print("출연 배우 :\t 정보 없음")
        directorList = "정보 없음"

    #장르
    try:
        genre = list[n].find(class_="info_txt1").find_all("dd")[0].find("span").find_all("a")
        genreList = [genre.text.strip() for genre in genre]
        print("장르 :\t",genreList)
    except IndexError:
        print("장르 :\t 정보 없음")
        genreList = "정보 없음"
