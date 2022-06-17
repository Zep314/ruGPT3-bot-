import os

from mylog import add2log
import telebot

from ruGPT3requests import generate_ruGPT3
#pip install pytelegrambotapi


#bot: telebot.TeleBot = telebot.TeleBot(token)
# Ключ не палите!!!!
bot = telebot.TeleBot('5387549008:AAEbiHRs9kivi1OPqWK9CG6XewqFrIbmhVg')
mode: bool = False

@bot.message_handler(commands=['help'])
def send_start_message(message):
    bot.reply_to(message, 'ИИ сочинятель текстов.\n'
                          'Напиши первые предложения для генерации текста\n'
                          'Для получения справки - /help\n'
                          'Для получения информации - /info\n'
                          'Включить генерацию текста - /activate\n'
                          'Отлючить генерацию текста - /deactivate'
                )

@bot.message_handler(commands=['info'])
def send_help_message(message):
    bot.reply_to(message, 'Бот для генерации текстов.\n'
                          'Написан командой из 4-х человек\n'
                          'Используется модель ruGPT3 от Сбербанка\n'
                     )

@bot.message_handler(commands=['activate'])
def send_activate_bot(message):
    global mode 
    mode = True
    bot.reply_to(message, 'Бот включен')

@bot.message_handler(commands=['deactivate'])
def send_deactivate_bot(message):
    global mode 
    mode= False
    bot.reply_to(message, 'Бот выключен')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if mode:
        add2log('<'+message.text)
        bot.send_chat_action(message.chat.id, 'typing')
        text = generate_ruGPT3(message.text)
        bot.send_message(message.chat.id,text)
        add2log('>'+text)
    else:
        add2log('<'+message.text)
        bot.reply_to(message, message.text)
        bot.send_message(message.chat.id,'Непонятно... Напиши /help - для помощи')

