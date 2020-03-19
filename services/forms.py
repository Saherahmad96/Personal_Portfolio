from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

# EXAMPLE | Api Route for Getting the weather data
@dashboard.route('/altGetWeatherData', methods=['GET'])
def altGetWeatherData():
	url = "https://api.darksky.net/forecast/6f5d06c8550c54d468601ad72af413fd/33.9052,-84.0084"
	
	# Does a GET request to get the weather data
	r = requests.get(url)
	print (r.status_code)

	# Checks the request status to see if it pass
	if r.status_code == 200:
		apiData = r.json()
		return jsonify({'data': apiData, 'error':''})
	else:
		return jsonify({'error':'Failure to retreive weather data!'})
