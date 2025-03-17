import telebot
from telebot import types

#--Импорт библиотек

bot= telebot.TeleBot('Вставь сюда айпи :)))')

#-- Создание массивов с информацией
desc = {
    "Подъём": "9:25",
    "Занятие 1 - программирование": "10:50 - 12:10",
    "Обед": "12:40",
    "Школа": "13:20 - 19:00"

    
}

Понедельник = {
    1: "О важном",
    2: "Алгебра",
    3: "Физика",
    4: "Англ яз",
    5: "Англ яз",
    6: "Русский язык",
}

Вторник = {
    1: "Физ-ра",
    2: "Физ-ра",
    3: "Геометрия",
    4: "География",
    5: "Русский язык",
    6: "Литература",
}

Среда = {
    1: "Труды",
    2: "Труды",
    3: "Русский зык",
    4: "Осл",
    5: "Биология",
    6: "Статистика вероятности",
}

Четверг = {
    1: "Функ грамм",
    2: "Русский язык",
    3: "Физика",
    4: "Общество",
    5: "История",
    6: "Геометрия",
}

Пятница = {
    1: "Алгебра",
    2: "Алгебра",
    3: "Музыка",
    4: "Литература",
    5: "Изо",
    6: "Информатика",
}

#-- Начальное сообщение
@bot.message_handler(commands= ['start']) #-- держатель для сообщения, чтобы бот понимал какая команды к чему
def start(message): #-- Всё, что находится в сообщение
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #--Markup - держит кнопки. items - информация в кнопках. markup.add - добавление кнопок в держатель
    item1 = types.KeyboardButton("Расписание на день")
    item2 = types.KeyboardButton("Расписание в школе")
    item3 = types.KeyboardButton("Дз")
    markup.add(item1, item2,item3)
    bot.send_message(message.chat.id, "Добро пожаловать, {0.username}".format(message.from_user),reply_markup=markup) #-- format для получения имя поьзователя. reply_markup -добавление держателя кнопок

@bot.message_handler(func=lambda message: message.text == "Расписание на день")
def show_desc(message):
    desc_text = "Расписание на день:\n" + "\n".join([f"{naming}: {time}." for naming, time in desc.items()]) #-- берет данные из массива и определяет что к чему относится 
    bot.send_message(message.chat.id, desc_text)

@bot.message_handler(func=lambda message: message.text == "Расписание в школе")
def What_day(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Monday = types.KeyboardButton("Понедельник")
    Tuesday = types.KeyboardButton("Вторник")
    Wednesday = types.KeyboardButton("Среда")
    Thursday = types.KeyboardButton("Четверг")
    Friday = types.KeyboardButton("Пятница")
    Go_back = types.KeyboardButton("Назад")
    markup.add(Monday,Tuesday,Wednesday,Thursday, Friday,Go_back)
    bot.send_message(message.chat.id, "Рассписание на какой день?",reply_markup=markup)

@bot.message_handler(func=lambda message:message.text == "Понедельник")
def monday(message):
       Monday_text = "Расписание на понедельник:\n" + "\n".join([f"{number} : {urok}." for number, urok in Понедельник.items()])
       bot.send_message(message.chat.id, Monday_text)

@bot.message_handler(func=lambda message:message.text == "Вторник")
def tuesday(message):
       tuesday_text = "Расписание на вторник:\n" + "\n".join([f"{number} : {urok}." for number, urok in Вторник.items()])
       bot.send_message(message.chat.id, tuesday_text)

@bot.message_handler(func=lambda message:message.text == "Среда")
def wednesday(message):
       wednesday_text = "Расписание на среду:\n" + "\n".join([f"{number} : {urok}." for number, urok in Среда.items()])
       bot.send_message(message.chat.id, wednesday_text)

@bot.message_handler(func=lambda message:message.text == "Четверг")
def thursday(message):
       thursday_text = "Расписание на четверг:\n" + "\n".join([f"{number} : {urok}." for number, urok in Четверг.items()])
       bot.send_message(message.chat.id, thursday_text)

@bot.message_handler(func=lambda message:message.text == "Пятница")
def friday(message):
       friday_text = "Расписание на пятницу:\n" + "\n".join([f"{number} : {urok}." for number, urok in Пятница.items()])
       bot.send_message(message.chat.id, friday_text)

@bot.message_handler(func=lambda message:message.text == "Дз")
def Homework (message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Дз")
    item2 = types.KeyboardButton("Назад")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Ссылка на домашнее задание: https://sgo.tomedu.ru/authorize/login",reply_markup=markup) 

@bot.message_handler(func=lambda message:message.text == "Назад")
def Wha (message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Расписание на день")
    item2 = types.KeyboardButton("Расписание в школе")
    item3 = types.KeyboardButton("Дз")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id,"Добро пожаловать, {0.username}".format(message.from_user),reply_markup=markup) 

bot.polling() #-- Иницилизация бота чтобы оно в общем работало
    