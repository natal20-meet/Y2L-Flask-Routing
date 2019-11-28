from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *
app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


##### Code here ######
@app.route('/')
def home():
	return render_template("home.html")

@app.route('/store')
def store():

	products = query_products()
	return render_template('store.html', products = products)
@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/cart')
def cart():
	return render_template('cart.html')

@app.route('/cart/<name>')
def cart1(name):
	
	return render_template('store.html', product = name)







#####################


if __name__ == '__main__':
    app.run(debug=True)