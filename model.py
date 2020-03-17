from pymongo import MongoClient
import os, requests, pymongo

def connectToDB():
	client = MongoClient('localhost', 27017)
	db = client.saher
	return db