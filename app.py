from flask import Flask, render_template, jsonify, url_for, request, flash, redirect, session, abort
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
import pymongo
from pymongo import MongoClient
import os

client = MongoClient('localhost', 27017)
db = client.saher
collection = db.data

Portfolio = Flask(__name__)

@Portfolio.route('/Homepage')
def Homepage():
    return render_template('home.html', name='Saher')

@Portfolio.route('/AboutMe')
def AboutMe():
    return render_template('aboutme.html', name='Saher')

@Portfolio.route('/ContactForm', methods=['GET', 'POST'])
def ContactForm():
	return render_template('contactform.html', name='Saher')

	if request.method == 'GET':
		print('Submitted')
		Data = [
			{   
				'Name':'Saher',
				'Phone':'xxx-xxx-xxxx',
				'Email':'saher@gmail.com',
			},
				
			{
				'Name':'sam1232',
				'Phone':'xxx-xxx-xxxx',
				'Email':'sam@gmail.com',
			},
			]
		print(Data)
		return jsonify(Data)
		if request.method == 'POST':
			return jsonify('NA')

@Portfolio.route('/MyPortfolio')
def ShowPortfolio():
    return render_template('portfolio.html', name='Saher')

@Portfolio.route('/Google')
def API():
    return render_template('API.html', name='Saher')

def getWeatherData():
	url = "https://www.weatherData.com/api"
	headers = {'content-type':'application/josn', 'authorization':'Bearer AIzaSyBPy5d7wOF9QkK7XT1Vt76iFwDs7mHx2g0'}

	# Does a GET request to get the weather data
	r = request.get(url, headers)

	# Assigns the status of the request to a variable
	r = apiRequest.status()		200 400 500

	# Checks the request status to see if it pass
	if r == 200:
		apiData = r.json()
		return {'data': apiData, 'error':''}
	else:
		return {'error':'Failure to retreive weather data!'}

@Portfolio.route('/showWeatherData')
def showWeatherData():
	weatherData = getWeatherData()
	print(weatherData)
	
	if 'data' in weatherData:
		weatherData = weatherData['data']
		return render_template('weatherWidget.html', data=weatherData)
	else:
		weatherError = weatherData['error']
		return render_template('weatherWidget.html', error=weatherError)

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

@Portfolio.route('/')
def home():
	return render_template('login.html')
		
@Portfolio.route('/login', methods=['POST'])
def admin_login():
	if request.form['password'] == 'password' and request.form['username'] == 'admin':
		session['logged_in'] = True

if __name__ == '__main__':
    Portfolio.run()

