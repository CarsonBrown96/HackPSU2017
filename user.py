import json
import decoder
import os

class User:
	def __init__(self, uid, calorie_goal):
		self.uid = uid
		self.calorie_goal = calorie_goal

def getUser(message):
	return getUserInfo(get_userid(message))

def getUserInfo(id):
	filename = 'users.json'
	with open(filename, 'r') as f:
		data = json.load(f)
		for user in data['users']:
			if user['id'] == id:
				return user['caloriesG'], user['caloriesT']
		f['users'].push({"id":id, "caloriesG":"0", "caloriesT": "0"})
		return "0", "0"

def addCalories(cal, id):
	filename = 'users.json'
	with open(filename, 'r') as f:
		data = json.load(f)
		for user in data['users']:
			if user['id'] == id:
				user['caloriesT'] = int(user['caloriesT']) + cal
	with open(filename, 'w') as f:
		f.write(json.dumps(data))


if __name__ == "__main__":
	getUser(1234)