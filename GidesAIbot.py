#код самой крутой нейросети (нет)
import os
import telebot
import random
import time
from icrawler.builtin import GoogleImageCrawler

bot = telebot.TeleBot('г9pлЇl»ћ`3lyшџ±’—шБ][ЕОi')

files = os.listdir()
files.pop(files.index("GidesAIbot.py"))
for file in files:
	files[files.index(file)] = file.replace(".png","")
print(files)

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,"Привет, напиши любое сообщение и я постараюсь его превратить в картинку")

@bot.message_handler(content_types=['text'])
def message_handler(message):
	bot.send_message(message.chat.id,"Генерация изображения, это займет от 1 до 5 секунд")
	time.sleep(random.randint(1,5))
	if message.text in files:
		#print(message.text['text'])
		print(message.text)
		photo = open(f"{message.text}.png", 'rb')
		bot.send_photo(message.chat.id, photo)
	else:
		j = ","
		crawler = GoogleImageCrawler(storage={"root_dir":f"./"})
		crawler.crawl(keyword=message.text, max_num=1)
		files1 = os.listdir()
		for file in files1:
			if "000001" in file:
				f = file
		try:
			with open(f, 'rb') as photo:
				bot.send_photo(message.chat.id, photo)
			try:
				os.remove(f)
			except WindowsError:
				bot.send_message(message.chat.id,"Вы задаете запросы слишком часто")
				try:
					os.remove(f)
				except WindowsError:
					files2 = os.listdir()
					for file in files2:
						if "000001" in file:
							os.remove(file)
				return
		except:
			bot.send_message(message.chat.id,"Не удалось сгенерировать картинку, попробуйте еще раз")

		#bot.send_message(message.chat.id,f"Помните что бот находится в бета тестировании, попробуйте задать такие запросы:\n {j.join(files)}")
	


bot.polling(none_stop=True)
