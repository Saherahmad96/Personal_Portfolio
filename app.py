from flask import Flask, render_template, jsonify, url_for
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.saher
collection = db.contact_data
contact_data = [
		{
			'Name':'Saher',
			'Phone':'xxx-xxx-xxxx',
			'Email':'saher@gmail.com',
		},
		{
			'Name':'sam1232',
			'Phone':'xxx-xxx-xxxx',
			'Email':'sam@gmail.com',
		}
	]
collection.insert_many(contact_data, ordered=False)

Portfolio = Flask(__name__)

@Portfolio.route('/Homepage')
def Homepage():
    return render_template('home.html', name='Saher')

@Portfolio.route('/AboutMe')
def AboutMe():
    return render_template('aboutme.html', name='Saher')

@Portfolio.route('/ContactForm')
def ContactForm():
    return render_template('contactform.html', name='Saher')

@Portfolio.route('/MyPortfolio')
def ShowPortfolio():
    return render_template('portfolio.html', name='Saher')

@Portfolio.route('/Google')
def API():
    return render_template('API.html', name='Saher')

@Portfolio.route('/handleContactForm')
def handleContactForm():
    # Get JSON DATA from front end

    print (data)

if __name__ == '__main__':
    Portfolio.run()

