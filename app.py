from flask import Flask, Blueprint, render_template, jsonify, url_for, request, redirect, session
from dash.views import dashboard
from contact.views import contact

# Sets up a new flask app
Portfolio = Flask(__name__)

# Registers blueprints
Portfolio.register_blueprint(dashboard)
Portfolio.register_blueprint(contact)

@Portfolio.route('/')
def Homepage():
    return render_template('home.html', name='Saher')

@Portfolio.route('/AboutMe')
def AboutMe():
    return render_template('aboutme.html', name='Saher')

@Portfolio.route('/MyPortfolio')
def ShowPortfolio():
    return render_template('portfolio.html', name='Saher')

if __name__ == '__main__':
    Portfolio.run(debug=True)

