import telebot
from telebot import types # для указание типов
import rqst


# constants for rqst
event1 = 'depart'
event2 = 'arr'




bot = telebot.TeleBot('6270091840:AAGTuqNNf4LrtiaLrJJzNigvVZmameg9jyM')
class telebot_itmo:
    @bot.message_handler(commands=['start'])
    def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👋 Поздороваться")
        btn2 = types.KeyboardButton("🛤️ узнать расписание")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот для проекта по питону".format(message.from_user), reply_markup=markup)
        
    @bot.message_handler(content_types=['text'])
    def func(message):
        print(message.text)
        if(message.text == "👋 Поздороваться"):
            bot.send_message(message.chat.id, text="Привеет.. Какая для вас идеальная мужская фигура? Например: квадрат)")
        elif(message.text == "🛤️ узнать расписание"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("🚃 ж/д рейсы")
            btn2 = types.KeyboardButton("✈️ авиарейсы")
            back = types.KeyboardButton("🛑 Вернуться в главное меню") 
            markup.add(btn1, btn2, back)
            bot.send_message(message.chat.id, text="Выберите тип транспорта: ", reply_markup=markup)
        
        #-----авиарейсы-----#
        
        elif(message.text == "✈️ авиарейсы"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("🛫 вылет")
            btn2 = types.KeyboardButton("🛬 приземление")
            back = types.KeyboardButton("🛑 Вернуться в главное меню") 
            markup.add(btn1, btn2, back)
            bot.send_message(message.chat.id, text = 'Вы хотите вылет или приземление?',parse_mode = 'HTML',reply_markup=markup)
            
        elif(message.text == '🛬 приземление'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("💬 приземление в ближайшие 2 часа")
            btn2 = types.KeyboardButton("📝 приземление на весь день")
            back = types.KeyboardButton("🛑 Вернуться в главное меню") 
            markup.add(btn1, btn2, back)
            bot.send_message(message.chat.id, text = 'Выберете время приземление:',reply_markup=markup)
        
        elif(message.text == '🛫 вылет'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("💬 вылет в ближайшие 2 часа")
            btn2 = types.KeyboardButton("📝 вылет на весь день")
            back = types.KeyboardButton("🛑 Вернуться в главное меню") 
            markup.add(btn1, btn2, back)
            bot.send_message(message.chat.id, text = 'Выберете время вылета:',reply_markup=markup)
            
        elif(message.text == '💬 приземление в ближайшие 2 часа'):
            bot.send_message(message.chat.id, text = '',reply_markup=markup)
        elif(message.text == '📝 приземление на весь день'):
            bot.send_bot.send_document(message.chat.id, open(r'Путь_к_документу/Название_документа.txt', 'rb'))
        elif(message.text == '💬 вылет в ближайшие 2 часа'):
            bot.send_message(message.chat.id, text = '',reply_markup=markup)
        elif(message.text == '📝 вылет на весь день'):
            bot.send_bot.send_document(message.chat.id, open(r'Путь_к_документу/Название_документа.txt', 'rb'))
            
        #-----железнодорожные рейсы-----#    
            
        elif message.text == "🚃 ж/д рейсы":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("🚉 отправление")
            btn2 = types.KeyboardButton("🚂 прибытие")
            back = types.KeyboardButton("🛑 Вернуться в главное меню") 
            markup.add(btn1, btn2, back)
            bot.send_message(message.chat.id, text= rqst.train_table(rqst.station_code ,rqst.event),parse_mode = 'HTML',reply_markup=markup)
            
        elif(message.text == '🚂 прибытие'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("💬 прибытие в ближайшие 2 часа")
            btn2 = types.KeyboardButton("📝 прибытие на весь день")
            back = types.KeyboardButton("🛑 Вернуться в главное меню") 
            markup.add(btn1, btn2, back)
            bot.send_message(message.chat.id, text = 'Выберете время приземление:',reply_markup=markup)
        
        elif(message.text == '🚉 отправление'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("💬 отправление в ближайшие 2 часа")
            btn2 = types.KeyboardButton("📝 отправление на весь день")
            back = types.KeyboardButton("🛑 Вернуться в главное меню") 
            markup.add(btn1, btn2, back)
            bot.send_message(message.chat.id, text = 'Выберете время вылета:',reply_markup=markup)
            
        elif(message.text == '💬 прибытие в ближайшие 2 часа'):
            bot.send_message(message.chat.id, text = '',reply_markup=markup)
        elif(message.text == '📝 прибытие на весь день'):
            bot.send_bot.send_document(message.chat.id, open(r'Путь_к_документу/Название_документа.txt', 'rb'))
        elif(message.text == '💬 отправление в ближайшие 2 часа'):
            bot.send_message(message.chat.id, text = '',reply_markup=markup)
        elif(message.text == '📝 отправление на весь день'):
            bot.send_bot.send_document(message.chat.id, open(r'Путь_к_документу/Название_документа.txt', 'rb'))
        
        elif (message.text == "🛑 Вернуться в главное меню"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("👋 Поздороваться")
            button2 = types.KeyboardButton("🛤️ узнать расписание")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован..")
if __name__ == "__main__":
    bot.polling(none_stop=True)  