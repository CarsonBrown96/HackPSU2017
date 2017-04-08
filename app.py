import os, sys
from flask import Flask, request
from pymessenger import Bot
import decoder
import response
import split_text
import nutritionseach

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAECxaoUf2UBAL987CccjNQxbpomeZCoPeaVCzFDKgbEUfwPhWaUmuMTGmylUiC3wXZCFbe5sNAbO5IBbl5onfftWQAPNMsUeGDpBACcKpeZAdU653TFnGSzvXIYmVLEYxNv69gTtaCTOP6azs4Sa7nPhq0WaO1LUNkbOfLPgZDZD"

bot = Bot(PAGE_ACCESS_TOKEN)

@app.route('/', methods=['GET'])
def verify():
	# Webhook verification
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.verify_token") == "HackPSU":
			return "Verification token mismatch", 403
		return request.args["hub.challenge"], 200
	return "Hello world", 200

@app.route('/', methods=['POST'])
def webhook():
	data = request.get_json()
	
	userid = decoder.get_userid(data)
	meals = nutritionseach.get_meals(decoder.get_text(data))

	respond = response.getResponse(userid, meals)

	bot.send_text_message(userid, respond)

	return "ok", 200

# def log(message):
# 	print(message)
# 	sys.stdout.flush()

if __name__ == "__main__":
	app.run(debug = True, port = 5000)