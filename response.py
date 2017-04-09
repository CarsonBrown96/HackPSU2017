import user

def getResponse(uid, meal):
	response = ''
	total = getTotal(meal)
	user.addCalories(total, uid)
	goal, total = user.getUserInfo(uid)
	for i in meal:
		response = response + str(i[0]) + ": " + str(int(i[1])) + " calories\n"
	response = response + "\n"
	response = response + "You have consumed " + str(int(total)) + " of your " + str(int(goal)) + " daily calories\n"
	response = response + "That is " + str(int(float(total) / float(goal) * 100)) + "% of your daily intake"
	return response

def getTotal(meal):
	sum = 0
	for i in meal:
		sum = sum + i[1]
	return sum
