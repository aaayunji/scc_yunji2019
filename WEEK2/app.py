from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

name = 'default'
age = 0
articles = []
articles_idx = 0

## HTML 주는 부분::새로만든
@app.route('/')
def home():
    return 'This is Home!'

@app.route('/mypage')
def mypage():
    return render_template('index.html')

## API 역할 하는 부분
@app.route('/test', methods=['POST'])
def test_post():

    # name give를 받는 부분
    name_receive = request.form['name_give']

    # global 변수 name에 받은 것을 덮어쓰기
    global name
    name = name_receive

    return jsonify({'result':'success','msg':'이 요청은 POST!', name:name})

@app.route('/test', methods=['GET'])
def test_get():
    global name
    global age
    name = request.args.get('name')
    age = request.args.get('age')

    return jsonify({'result':'success','msg':'이 요청은 GET!',name:name,age:age})

@app.route('/post',methods=['POST'])
def post_save():

    global articles
    global articles_idx
    link = request.form['link']  #사용자가 body에 담은 데이터를 가지고 오는 것
    comment = request.form['comment']
    articles_idx = articles_idx +1

    article = {'articles_idx' : articles_idx+1,'link':link, 'comment':comment}
    articles.append(article)

    return jsonify({'result':'success'})

@app.route('/view',methods=['GET'])
def get_view():
    return jsonify({'result':'success','data':articles})

@app.route('/delete', methods=['POST'])
def post_delete():
    global articles
    articles_idx = request.form['articles_idx']

    for article in articles:
        if str(article['articles_idx']) == articles_idx:
            articles.remove(article)
            return jsonify({'result':'success'})
    return jsonify({'result':'success','data':'articles'})

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)

