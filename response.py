import user

def getResponse(uid, meal):
	response = ''
	total = getTotal(meal)
	addCalories(uid, total)
	goal, total = getUserInfo(uid)
	for i in meal:
		response = response + meal[0] + ": " + meal[1] + " calories\n"
	response = response + "\n"
	response = response + "You have consumed " + total + " of your " + goal + " daily calories\n"
	response = response + "That is " + str(int(float(total) / float(goal) * 100)) + "\% of your daily intake"
	return response

def getTotal(meal):
	sum = 0
	for i in meal:
		sum = sum + i[1]
	return sum