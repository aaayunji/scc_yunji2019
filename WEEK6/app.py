from bs4 import BeautifulSoup
import urllib.request

html = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn#')
soup = BeautifulSoup(html,'lxml')


#dt class명이 tit_t1인 <a>태그의 이름을 가져와라 --> 장르명 가져오기
# 그 장르 데이터를 다 모아서 순위대로 영화를 보여주기

# 장르 버튼 5개는 액션, 코미디, SF, 드라마, 멜로/로맨스
# 유저에게 장르별 버튼 클릭을 받아서 내보낼때는 각각 장르별 영화 정보만 순위대로 노출 (영화 포스터, 제목, 감독, 출연자)

# + 줄거리보기 버튼을 만들어서 팝업 페이지로 연결시키기

##영화장르
genres = soup.find_all('span','link_txt')
print (genres[0].find('a').text)
rank = 1

##영화제목
titles = soup.find_all('dt','tit')
print (titles[0].find('a').text)
rank = 1



#
# for title in titles:
#     print(title.find('a').text)
#     rank += 1

# for title in titles:
#     print(str(rank) + "위 : " + title.find('a').text)
#     rank += 1


#
# for genre in genres:
#     print(genre.find('a').text)
#     rank += 1

# ##영화감독
# titles = soup.find_all('dt','tit_t2')
#
# print (titles[0].find('a').text)
#
# rank = 1
#
# for title in titles:
#     print(title.find('a').text)
#     rank += 1
#
# ##영화출연자
# titles = soup.find_all('dt','tit_t3')
#
# print (titles[0].find('a').text)
#
# rank = 1
#
# for title in titles:
#     print(title.find('a').text)
#     rank += 1