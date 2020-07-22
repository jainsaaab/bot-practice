from telegram.ext import Updater, CommandHandler
import requests
import re

def getUrl():
	contents = requests.get('https://random.dog/woof.json').json()
	image_url = contents['url']
	return image_url

def bop(bot, update):
	url = getUrl()
	chat_id = update.message.chat_id
	print(chat_id)
	bot.send_photo(chat_id=chat_id, photo=url)

def main():
	updater = Updater('1394221851:AAFnfzO-q0bzvCb3LQ622SmhRauC78ACgLM')
	dp = updater.dispatcher
	dp.add_handler(CommandHandler("bop", bop))
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()
