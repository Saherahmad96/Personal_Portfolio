from pymongo import MongoClient
import os, requests, pymongo
from flask import Flask, render_template, jsonify, url_for, request, flash, redirect, session, abort
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

Portfolio = Flask(__name__)

"""
Examples for for loops 

for item in data:
	print(item)

for i in range(0, len(data)):
	currentData = data[i]
	print(currentData)

"""

def connectToDB():
	client = MongoClient('localhost', 27017)
	db = client.saher
	return db

@Portfolio.route('/altGetWeatherData', methods=['GET'])
def altGetWeatherData():
	url = "https://api.darksky.net/forecast/6f5d06c8550c54d468601ad72af413fd/33.9052,-84.0084"
	
	#headers = {'content-type':'application/josn', 'authorization':'Bearer AIzaSyBPy5d7wOF9QkK7XT1Vt76iFwDs7mHx2g0'}

	# Does a GET request to get the weather data
	r = requests.get(url)
	print (r.status_code)

	# Checks the request status to see if it pass
	if r.status_code == 200:
		apiData = r.json()
		return jsonify({'data': apiData, 'error':''})
	else:
		return jsonify({'error':'Failure to retreive weather data!'})

def getWeatherData():
	url = "https://api.darksky.net/forecast/6f5d06c8550c54d468601ad72af413fd/33.9052,-84.0084"
	
	#headers = {'content-type':'application/josn', 'authorization':'Bearer AIzaSyBPy5d7wOF9QkK7XT1Vt76iFwDs7mHx2g0'}

	# Does a GET request to get the weather data
	r = requests.get(url)
	print (r.status_code)

	# Checks the request status to see if it pass
	if r.status_code == 200:
		apiData = r.json()
		return {'data': apiData, 'error':''}
	else:
		return {'error':'Failure to retreive weather data!'}


@Portfolio.route('/showWeatherData', methods=['GET'])
def showWeatherData():
	weatherData = getWeatherData()
	
	if 'data' in weatherData:
		weatherData = weatherData['data']
		return render_template('weatherWidget.html', data=weatherData)
	else:
		weatherError = weatherData['error']
		return render_template('weatherWidget.html', error=weatherError)


@Portfolio.route('/altGetNewsData', methods=['GET'])
def altGetNewsData():
	url = "http://newsapi.org/v2/top-headlines?country=us&apiKey=0a27659cc5a24df2bfdda7d5201f201c"
	
	a = requests.get(url)
	print (a.status_code)

	if a.status_code == 200:
		apiData1 = a.json()
		return jsonify({'infodata': apiData1, 'error':''})
	else:
		return jsonify({'error':'Failure to retreive news data!'})

def getNewsData():
	url = "http://newsapi.org/v2/top-headlines?country=us&apiKey=0a27659cc5a24df2bfdda7d5201f201c"
	
	a = requests.get(url)
	print (a.status_code)

	if a.status_code == 200:
		apiData1 = a.json()
		return {'infodata': apiData1, 'error':''}
	else:
		return {'error':'Failure to retreive news data!'}

@Portfolio.route('/showNewsData', methods=['GET'])
def showNewsData():
	newsData = getNewsData()
	
	if 'infodata' in newsData:
		newsData = newsData['infodata']
		return render_template('dashboard.html', infodata=newsData)
	else:
		newsError = newsData['error']
		return render_template('dashboard.html', error=newsError)


@Portfolio.route('/')
def home():
	return render_template('login.html')
		
@Portfolio.route('/login', methods=['POST'])
def admin_login():
	if request.form['password'] == 'password' and request.form['username'] == 'admin':
		session['logged_in'] = True

@Portfolio.route('/Homepage')
def Homepage():
    return render_template('home.html', name='Saher')

@Portfolio.route('/AboutMe')
def AboutMe():
    return render_template('aboutme.html', name='Saher')

@Portfolio.route('/MyPortfolio')
def ShowPortfolio():
    return render_template('portfolio.html', name='Saher')

@Portfolio.route('/Google')
def API():
    return render_template('API.html', name='Saher')

@Portfolio.route('/ContactForm', methods=['GET', 'POST'])
def ContactForm():
	return render_template('contactform.html', name='Saher')

@Portfolio.route('/handleContactForm', methods=['POST'])
def handleContactForm():
	try:
		# Get front end data
		ajax_data = request.get_json()
		print(ajax_data)

		# Connect to my database and correct collection
		db = connectToDB()
		contact_data = db.contact_data

		#Insert form data into db
		contact_data.insert_one(ajax_data)

		# Return success message
		return jsonify('Successful!')
	except Exception as e:
		print(str(e))
		return jsonify('Failed')

if __name__ == '__main__':
    Portfolio.run(debug=True)

