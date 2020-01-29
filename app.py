from flask import Flask, render_template, jsonify
import pymongo

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

if __name__ == '__main__':
    Portfolio.run()

