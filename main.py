import telebot
from telebot import types

import messages

bot = telebot.TeleBot('7628835733:AAFWOz-YjLUz2LWLQ_thPA26afj-uJtAD1I')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup() #Markup для первого сообщения
    btn1 = types.InlineKeyboardButton("⚫ DELUXE ⚫", callback_data="delux")                                       #текст кнопок
    btn2 = types.InlineKeyboardButton("🟡 EXTRA 🟡", callback_data="extra")
    btn3 = types.InlineKeyboardButton("⚪ ESSENTIAL ⚪", callback_data="essen")
    btn4 = types.InlineKeyboardButton("🔹 EA PLAY 🔹", callback_data="eplay")
    markup.add(btn1, btn2, btn3, btn4)                                                                            #Добавляем кнопки под сообщение
    bot.send_message(message.from_user.id, messages.start_message, reply_markup=markup)                                 #Текст сообщения

@bot.callback_query_handler(func=lambda callback: True)
def callback_check(callback):
    if callback.data == "delux":                                                                                        #Сообщение при выборе Deluxe
        btnDX1 = types.InlineKeyboardButton("1 месяц", callback_data="dx1")
        btnDX3 = types.InlineKeyboardButton("3 месяца", callback_data="dx3")
        btnDX12 = types.InlineKeyboardButton("12 месяцев", callback_data="dx12")
        btnBack = types.InlineKeyboardButton("Назад", callback_data="backmenu")
        markup = types.InlineKeyboardMarkup()
        markup.add(btnDX1, btnDX3, btnDX12, btnBack)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)                            #Удаление пердыдущего сообщения
        bot.send_message(chat_id=callback.message.chat.id, text=messages.answer_delux, reply_markup=markup)                                                                                 #Текст сообщения

    elif callback.data == "extra":                                                                                      #Сообщение при выборе Extra
        btnDX1 = types.InlineKeyboardButton("1 месяц", callback_data="ex1")
        btnDX3 = types.InlineKeyboardButton("3 месяца", callback_data="ex3")
        btnDX12 = types.InlineKeyboardButton("12 месяцев", callback_data="ex12")
        btnBack = types.InlineKeyboardButton("Назад", callback_data="backmenu")
        markup = types.InlineKeyboardMarkup()
        markup.add(btnDX1, btnDX3, btnDX12, btnBack)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)                            #Удаление пердыдущего сообщения
        bot.send_message(chat_id=callback.message.chat.id, text=messages.answer_extra, reply_markup=markup)                                                                                   #Текст сообщения

    elif callback.data == "essen":                                                                                      #Сообщение при выборе Essential
        btnDX1 = types.InlineKeyboardButton("1 месяц", callback_data="es1")
        btnDX3 = types.InlineKeyboardButton("3 месяца", callback_data="es3")
        btnDX12 = types.InlineKeyboardButton("12 месяцев", callback_data="es12")
        btnBack = types.InlineKeyboardButton("Назад", callback_data="backmenu")
        markup = types.InlineKeyboardMarkup()
        markup.add(btnDX1, btnDX3, btnDX12, btnBack)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)                            #Удаление пердыдущего сообщения
        bot.send_message(chat_id=callback.message.chat.id, text=messages.answer_essen, reply_markup=markup)                                                                                     #Текст сообщения

    elif callback.data == "eplay":                                                                                      #Сообщение при выборе EA Play
        btnDX1 = types.InlineKeyboardButton("1 месяц", callback_data="ea1")
        btnDX3 = types.InlineKeyboardButton("3 месяца", callback_data="ea3")
        btnDX12 = types.InlineKeyboardButton("12 месяцев", callback_data="ea12")
        btnBack = types.InlineKeyboardButton("Назад", callback_data="backmenu")
        markup = types.InlineKeyboardMarkup()
        markup.add(btnDX1, btnDX3, btnDX12, btnBack)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)                            #Удаление пердыдущего сообщения
        bot.send_message(chat_id=callback.message.chat.id, text=messages.answer_eplay, reply_markup=markup)                                                                                 #Текст сообщения

    elif callback.data == "dx1":                                                                                        #Сообщение при выборе Deluxe 1 месяц
        btnBack = types.InlineKeyboardButton("Назад", callback_data="delux")
        markup = types.InlineKeyboardMarkup()
        markup.add(btnBack)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)                            #Удаление пердыдущего сообщения
        bot.send_message(chat_id=callback.message.chat.id, text=messages.time_delux_1_month, reply_markup=markup)                                                                     #Текст сообщения

    elif callback.data == "dx3":                                                                                        #Сообщение при выборе Deluxe 3 месяца
        btnBack = types.InlineKeyboardButton("Назад", callback_data="delux")
        markup = types.InlineKeyboardMarkup()
        markup.add(btnBack)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)                            #Удаление пердыдущего сообщения
        bot.send_message(chat_id=callback.message.chat.id, text=messages.time_delux_3_month, reply_markup=markup)

    elif callback.data == "dx12":                                                                                       #Сообщение при выборе Deluxe 12 месяцев
        btnBack = types.InlineKeyboardButton("Назад", callback_data="delux")
        markup = types.InlineKeyboardMarkup()
        markup.add(btnBack)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)                            #Удаление пердыдущего сообщения
        bot.send_message(chat_id=callback.message.chat.id, text=messages.time_delux_12_month, reply_markup=markup)                                                                            #Текст сообщения

    elif callback.data == "ex1":                                                                                        #Сообщение при выборе Extra 1 месяц
        btnBack = types.InlineKeyboardButton("Назад", callback_data="extra")
        markup = types.InlineKeyboardMarkup()
        markup.add(btnBack)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)                            #Удаление пердыдущего сообщения
        bot.send_message(chat_id=callback.message.chat.id, text=messages.time_extra_1_month, reply_markup=markup)                                                                         #Текст сообщения

    elif callback.data == "ex3":                                                                                        #Сообщение при выборе Extra 3 месяца
        btnBack = types.InlineKeyboardButton("Назад", callback_data="extra")
        markup = types.InlineKeyboardMarkup()
        markup.add(btnBack)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)                            #Удаление пердыдущего сообщения
        bot.send_message(chat_id=callback.message.chat.id, text=messages.time_extra_3_month, reply_markup=markup)                                                                         #Текст сообщения

    elif callback.data == "ex12":                                                                                        #Сообщение при выборе Extra 12 месяцев
        btnBack = types.InlineKeyboardButton("Назад", callback_data="extra")
        markup = types.InlineKeyboardMarkup()
        markup.add(btnBack)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)                            #Удаление пердыдущего сообщения
        bot.send_message(chat_id=callback.message.chat.id, text=messages.time_extra_12_month, reply_markup=markup)                                                                             #Текст сообщения

    elif callback.data == "es1":                                                                                        #Сообщение при выборе Essential 1 месяц
        btnBack = types.InlineKeyboardButton("Назад", callback_data="essen")
        markup = types.InlineKeyboardMarkup()
        markup.add(btnBack)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)                            #Удаление пердыдущего сообщения
        bot.send_message(chat_id=callback.message.chat.id, text=messages.time_essen_1_month, reply_markup=markup)                                                                        #Текст сообщения

    elif callback.data == "es3":                                                                                        #Сообщение при выборе Essential 3 месяца
        btnBack = types.InlineKeyboardButton("Назад", callback_data="essen")
        markup = types.InlineKeyboardMarkup()
        markup.add(btnBack)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)                            #Удаление пердыдущего сообщения
        bot.send_message(chat_id=callback.message.chat.id, text=messages.time_essen_3_month, reply_markup=markup)                                                                           #Текст сообщения

    elif callback.data == "es12":                                                                                        #Сообщение при выборе Essential 12 месяцев
        btnBack = types.InlineKeyboardButton("Назад", callback_data="essen")
        markup = types.InlineKeyboardMarkup()
        markup.add(btnBack)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)                            #Удаление пердыдущего сообщения
        bot.send_message(chat_id=callback.message.chat.id, text=messages.time_essen_12_month, reply_markup=markup)                                                                         #Текст сообщения

    elif callback.data == "ea1":                                                                                        #Сообщение при выборе EA Play 1 месяц
        btnBack = types.InlineKeyboardButton("Назад", callback_data="eplay")
        markup = types.InlineKeyboardMarkup()
        markup.add(btnBack)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)                            #Удаление пердыдущего сообщения
        bot.send_message(chat_id=callback.message.chat.id, text=messages.time_eplay_1_month, reply_markup=markup)                                                                          #Текст сообщения

    elif callback.data == "ea3":                                                                                        #Сообщение при выборе EA Play 3 месяца
        btnBack = types.InlineKeyboardButton("Назад", callback_data="eplay")
        markup = types.InlineKeyboardMarkup()
        markup.add(btnBack)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)                            #Удаление пердыдущего сообщения
        bot.send_message(chat_id=callback.message.chat.id, text=messages.time_eplay_3_month, reply_markup=markup)                                                                           #Текст сообщения

    elif callback.data == "ea12":                                                                                       #Сообщение при выборе EA Play 12 месяцев
        btnBack = types.InlineKeyboardButton("Назад", callback_data="eplay")
        markup = types.InlineKeyboardMarkup()
        markup.add(btnBack)
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)                            #Удаление пердыдущего сообщения
        bot.send_message(chat_id=callback.message.chat.id, text=messages.time_eplay_12_month, reply_markup=markup)                                                                           #Текст сообщения

    elif callback.data == "backmenu":
        markup = types.InlineKeyboardMarkup() #Markup для первого сообщения
        btn1 = types.InlineKeyboardButton("⚫ DELUXE ⚫", callback_data="delux")                                   #текст кнопок
        btn2 = types.InlineKeyboardButton("🟡 EXTRA 🟡", callback_data="extra")
        btn3 = types.InlineKeyboardButton("⚪ ESSENTIAL ⚪", callback_data="essen")
        btn4 = types.InlineKeyboardButton("🔹 EA PLAY 🔹", callback_data="eplay")
        markup.add(btn1, btn2, btn3, btn4)                                                                        #Добавляем кнопки под сообщение
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)                            #Удаление пердыдущего сообщения
        bot.send_message(chat_id=callback.message.chat.id, text=messages.start_message, reply_markup=markup)            #Текст сообщения


bot.polling(none_stop=True, interval=0)
