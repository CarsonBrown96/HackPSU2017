import json
import decoder
import os
import requests


def getUser(message):
	return getUserInfo(decoder.get_userid(message))

def getUserInfo(id):
	filename = 'users.json'
	with open(filename, 'r') as f:
		data = json.load(f)
		for user in data['users']:
			if user['id'] == id:
				return user['caloriesG'], user['caloriesT']
		a = {"id":id, "caloriesG":"2000", "caloriesT": "0"}
		data['users'].append(a)
	with open(filename, 'w') as f:
		f.write(json.dumps(data))
		return "2000", "0"

def addCalories(cal, id):
	filename = 'users.json'
	with open(filename, 'r') as f:
		data = json.load(f)
		for user in data['users']:
			if user['id'] == id:
				user['caloriesT'] = int(user['caloriesT']) + cal
	with open(filename, 'w') as f:
		f.write(json.dumps(data))

# def send_message(recipient_id, message):
# 	data = {
# 		"recipient":{"id": recipient_id},
# 		"message": {"text": message}
# 	}
# 	q = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + PAGE_ACCESS_TOKEN, json=data)
# 	if q.status_code != 200:
# 		log(q.status_code)
# 		log(q.text)

if __name__ == "__main__":
	getUser(1234)
