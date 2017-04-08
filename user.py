import json
import os

class User:
	def __init__(self, uid, calorie_goal):
		self.uid = uid
		self.calorie_goal = calorie_goal


def getUser(message):
	return getUserInfo(getUID(message))

def getUserInfo(id):
	filename = 'users.json'
	with open(filename, 'rw') as f:
		data = json.load(f)
		for user in data['users']:
			if user['id'] == id:
				return user['id'], user['caloriesG'], user['caloriesT']
		f['users'].push({"id":id, "caloriesG":"0", "caloriesT": "0"})
		return id, "0", "0"

if __name__ == "__main__":
	getUser(1234)