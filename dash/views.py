
import os, requests
from flask import Flask, Blueprint, render_template, jsonify, url_for, request, redirect, session
from .apiCalls import getWeatherData

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
def showAltWeatherData():
    return render_template('weatherWidget2.html')

@dashboard.route('/showNewsData', methods=['GET'])
def showNewsData():
	return render_template('news.html')

@dashboard.route('/showJobData', methods=['GET'])
def showJobData():
	return render_template('jobs.html')
