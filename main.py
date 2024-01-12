import telebot
from telebot import types
from config import TOKEN_API_KEY
from pdf import read_pdf
import re

bot = telebot.TeleBot(token=TOKEN_API_KEY)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=["document"])
def send_document(message):
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = "temp/"+str(message.from_user.id)+".pdf"
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    filename = str(message.from_user.id)
    bot.send_message(message.chat.id, read_pdf(src, str(message.from_user.id)))
    with open(f"temp/{filename}.txt", "r") as f:
        text = f.read()
        l = text.split("\n")
        for i in l:
            print(re.findall(string=text, pattern=r"\d\d\D\d\d\D\d\d")[0])
            print(i)
            if re.findall(string=text, pattern=r"\d\d\D\d\d\D\d\d")[0] in i:
                print(l.index(re.findall(string=text, pattern=i)))


bot.polling(none_stop=True)
