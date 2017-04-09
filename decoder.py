

""" Decodes a json object for the user id, timestamp and text """

def get_userid(json):
	return json['entry'][0]['messaging'][0]['sender']['id']

def get_timestamp(json):
	return json['entry'][0]['messaging'][0]['timestamp']
	 
def get_text(json):
	a = json['entry'][0]['messaging'][0]['message']['text']
	return a

