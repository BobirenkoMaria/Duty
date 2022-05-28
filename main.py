import telebot
from config import token
from sqlModel import *

Connect_db()

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Приветствую!")





bot.polling(none_stop=True)