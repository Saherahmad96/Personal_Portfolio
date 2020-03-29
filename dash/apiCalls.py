
import os, requests

# Example Api Call
def getWeatherData():
	url = "https://api.darksky.net/forecast/6f5d06c8550c54d468601ad72af413fd/33.9052,-84.0084"
	
	# Does a GET request to get the weather data
	r = requests.get(url)
	print (r.status_code)

	# Checks the request status to see if it pass
	if r.status_code == 200:
		apiData = r.json()
		return {'data': apiData, 'error':''}
	else:
		return {'error':'Failure to retreive weather data!'}


# EXAMPLE | Api Route for Getting the weather data
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

def jobData():
	i = requests.get('url')
	jobData = i.json()
	return(jobData) 

	if i.status_code == 500:
		return('error')
