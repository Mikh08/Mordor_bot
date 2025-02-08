import telebot
from telebot import types

bot = telebot.TeleBot('7628835733:AAFWOz-YjLUz2LWLQ_thPA26afj-uJtAD1I')


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("⚫ DELUXE ⚫")
    btn2 = types.KeyboardButton("🟡 EXTRA 🟡")
    btn3 = types.KeyboardButton("⚪ ESSENTIAL ⚪")
    btn4 = types.KeyboardButton("🔹 EA PLAY 🔹")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.from_user.id, '''👋 Добро пожаловать в наш магазин 👋
С помощью этого бота вы сможете приобрести подписку на Playstation
    
❓ Как это работает ❓
    
📍 Вы выбираете какую подписку и на какой срок хотите получить
📍 Бот выставляет вам счет на оплату
📍 После оплаты вы получаете подробную инструкцию по активации подписки
    
❌ Если возникнут сложности ❌
У нас есть активная и отзывчивая поддержка, которая поможет с решением любого вопроса! ''', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def buttons(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btnDX1 = types.InlineKeyboardButton("1 месяц", callback_data="dx1")
    btnDX3 = types.InlineKeyboardButton("3 месяца", callback_data="dx3")
    btnDX12 = types.InlineKeyboardButton("12 месяцев", callback_data="dx12")

    btnEX1 = types.InlineKeyboardButton("1 месяц", callback_data="ex1")
    btnEX3 = types.InlineKeyboardButton("3 месяца", callback_data="ex3")
    btnEX12 = types.InlineKeyboardButton("12 месяцев", callback_data="ex12")

    btnES1 = types.InlineKeyboardButton("1 месяц", callback_data="es1")
    btnES3 = types.InlineKeyboardButton("3 месяца", callback_data="es3")
    btnES12 = types.InlineKeyboardButton("12 месяцев", callback_data="es12")

    btnEAP1 = types.InlineKeyboardButton("1 месяц", callback_data="eap1")
    btnEAP3 = types.InlineKeyboardButton("3 месяца", callback_data="eap3")
    btnEAP12 = types.InlineKeyboardButton("12 месяцев", callback_data="eap12")

    btnBack = types.InlineKeyboardButton("Назад", callback_data="back")

    markup1.row(btnDX1, btnDX3, btnDX12, btnBack)
    markup2.row(btnEX1, btnEX3, btnEX12, btnBack)
    markup3.row(btnES1, btnES3, btnES12, btnBack)
    markup4.row(btnEAP1, btnEAP3, btnEAP12, btnBack)

    if (message.text == "⚫ DELUXE ⚫"):
        bot.send_message(message.chat.id, text='''Вы выбрали подписку: 
        
⚫ PS PLUS - DELUXE ⚫

Что входит в подписку:
 — Доступ к онлайн-игре
 — Скидки в PS Store
 — Классические игры с PS1-PS3
 — Пробные версии новинок
 — Более 700 игр в каталоге
 
Выберите срок подписки
''', reply_markup=markup1)
    elif (message.text == "🟡 EXTRA 🟡"):
        bot.send_message(message.chat.id, text='''Вы выбрали подписку: 
        
🟡 PS PLUS - EXTRA 🟡

Что входит в подписку:
— Доступ к онлайн-игре
— Скидки в PS Store
— Каталог из 400+ игр для PS4/PS5
 
Выберите срок подписки
''', reply_markup=markup2)
    elif (message.text == "⚪ ESSENTIAL ⚪"):
        bot.send_message(message.chat.id, text='''Вы выбрали подписку: 
        
⚪ PS PLUS - ESSENTIAL ⚪

Что входит в подписку:
— Доступ к онлайн-игре
— Скидки в PS Store
— 3 бесплатные игры каждый месяц
 
Выберите срок подписки
''', reply_markup=markup3)
    elif (message.text == "🔹 EA PLAY 🔹"):
        bot.send_message(message.chat.id, text='''Вы выбрали подписку: 
        
🔹 Playstation - EA PLAY 🔹

Что входит в подписку:
 — Хз
 
Выберите срок подписки
''', reply_markup=markup4)

@bot.callback_query_handler(func=lambda callback: True)
def callback_check(callback):
    if callback.data == "dx1":
        bot.sedit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text="Вы выбрали подписку: PS PLUS - DELUXE\nСрок: 1 месяц\nСтоимость: 159 рублей", reply_markup=None)

bot.polling(none_stop=True, interval=0)