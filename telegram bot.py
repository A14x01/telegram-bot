import telebot
import random

from telebot import types

bot = telebot.TeleBot('5863272101:AAEOn6C29bsoxR_ckigMlQplLYmK33tuKIk')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    sti = open('/Users/acvet/Downloads/Sticker1.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Random number')
    item2 = types.KeyboardButton('How are you?')

    markup.add(item1, item2)

    bot.reply_to(message, 'Welcome, {0.first_name}!\n Im <b>{1.first_name}</b> and Im created to be your puppet.'.format(message.from_user, bot.get_me()), parse_mode = 'html', reply_markup = markup)

@bot.message_handler(context_types = ['text'])
def lalala(message):
    if message.text == 'Random number':
        bot.send_message(message.chat.id, str(random.randit(0,100)))
    elif message.text == 'How are you?':
        bot.send_message(message.chat.id, 'Im good. What about you?')
    else:
        bot.send_message(message.chat.id, 'idk')


bot.infinity_polling()