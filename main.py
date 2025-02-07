import telebot
from telebot import types

bot = telebot.TeleBot('7628835733:AAFWOz-YjLUz2LWLQ_thPA26afj-uJtAD1I')


@bot.message_handler(commands=['start' , 'Menu'] , )
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("DELUXE")
    btn2 = types.KeyboardButton("EXTRA")
    btn3 = types.KeyboardButton("ESSENTIAL")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id, "Kupi pls", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def buttons(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btnD1 = types.KeyboardButton("1 месяц / 999р")
    btnD2 = types.KeyboardButton("12 месяцев / 4599р")
    btnStart = types.KeyboardButton("/Menu")
    btnEx2 = types.KeyboardButton("12 месяцев / 3199р")
    #btnE1 = types.KeyboardButton("1 месяц / 999р")
    btnE2 = types.KeyboardButton("12 месяцев / 2999р")
    markup1.add(btnD1, btnD2, btnStart)
    markup2.add(btnEx2)
    markup3.add(btnE2)

    if (message.text == "DELUXE"):
        bot.send_message(message.chat.id, text="PS PLUS DELUXE", reply_markup=markup1)
    elif (message.text == "EXTRA"):
        bot.send_message(message.chat.id, text="PS PLUS EXTRA", reply_markup=markup2)
    elif (message.text == "ESSENTIAL"):
        bot.send_message(message.chat.id, text="PS PLUS ESSENTIAL", reply_markup=markup3)


bot.polling(none_stop=True, interval=0)