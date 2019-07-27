from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


    @app.route('/save', method=['POST'])
    def save():
        url_receive = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190715'

        # db.lists.insert_one(list)


    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    # # select를 이용해서, tr들을 불러오기
    lists = soup.select('.music-list-wrap > tbody > tr')

    for list in lists:
        if not list.a == None:
            print (list.a.text)

# # URL을 읽어서 HTML를 받아오고,
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190715',headers=headers)
#
# # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup = BeautifulSoup(data.text, 'html.parser')
#
# # select를 이용해서, tr들을 불러오기
# movies = soup.select('#old_content > table > tbody > tr')
#
# # movies (tr들) 의 반복문을 돌리기
# for movie in movies:
# 		# movie 안에 a 가 있으면,
#     if not movie.a == None:
# 				# a의 text를 찍어본다.
#         print (movie.a.text)
#
# @app.route('/')
#
# def home():
#     return render_template('index.html')
#
    return jsonify({'result': 'success'})


# @app.route('/get',method=['GET'])
# def get():
#     return jsonify({'result':'success'})

