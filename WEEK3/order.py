from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

orders = []


@app.route('/order',methods=['POST'])
def post_order():

    global order_form

    name = request.form['name']
    quantity = request.form['quantity']
    address = request.form['address']
    phone = request.form['phone']

    order_form={'name':name ,'quantity':quantity,'address':address,'phone':phone}
    orders.append(order_form)

    return jsonify({'result':'success'})

@app.route('/view',methods=['GET'])
def get_view():

    return(jsonify({'result':'success','data':orders}))

@app.route('/')
def orderhome():
   return render_template('상품주문서.html')

@app.route('/order_list')
def order_list():
   return render_template('order_list.html')

if __name__ == '__main__':
    app.run('0.0.0.0',port=5002,debug=True)
