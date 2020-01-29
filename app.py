from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
import jinja2

Portfolio = Flask(__name__)

@Portfolio.route('/Homepage')
def Homepage();
    return render_template('home.html', name='Saher')

@Portfolio.route('/AboutMe')
def AboutMe():
    return render_template('aboutme.html', name='Saher')

@Portfolio.route('/ContactForm')
def AboutMe():
    return render_template('contactform.html', name='Saher')

@Portfolio.route('/Portfolio')
def AboutMe():
    return render_template('portfolio.html', name='Saher')

if__name__ == '__main__':
    Portfolio.run()

