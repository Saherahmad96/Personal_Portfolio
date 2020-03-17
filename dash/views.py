
import os, requests
from flask import Flask, Blueprint, render_template, jsonify, url_for, request, redirect, session
from apiCalls import getWeatherData

dashboard = Blueprint('dashboard', __name__, template_folder='templates', static_folder='static')

# EXAMPLE | Displays the Python Weather Widget
@dashboard.route('/showWeatherData', methods=['GET'])
def showWeatherData():
	weatherData = getWeatherData()
	
	if 'data' in weatherData:
		weatherData = weatherData['data']
		return render_template('weatherWidget.html', data=weatherData)
	else:
		weatherError = weatherData['error']
		return render_template('weatherWidget.html', error=weatherError)

# EXAMPLE | Displays the AJAX Weather Widget
@dashboard.route('/showAltWeatherData', methods=['GET'])
def showWeatherData():
    return render_template('weatherWidget2.html')

# EXAMPLE | Api Route for Getting the weather data
@dashboard.route('/altGetWeatherData', methods=['GET'])
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


