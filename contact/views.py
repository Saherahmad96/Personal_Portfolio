
import os, requests
from flask import Flask, Blueprint, render_template, jsonify, url_for, request, redirect, session
from model import connectToDB

contact = Blueprint('contact', __name__)

# Displays the Contact Form
@contact.route('/ContactForm', methods=['GET', 'POST'])
def ContactForm():
	return render_template('contactform.html', name='Saher')

#Api Route for Contact Form
@contact.route('/handleContactForm', methods=['POST'])
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