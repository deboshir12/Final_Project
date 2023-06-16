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
            rqst.flight_table(event2,2)
            bot.send_document(message.chat.id, open(r'schedule.txt', 'r'))
        elif(message.text == '📝 приземление на весь день'):
            rqst.flight_table(event2,24)
            bot.send_document(message.chat.id, open(r'schedule.txt', 'r'))
        elif(message.text == '💬 вылет в ближайшие 2 часа'):
            rqst.flight_table(event1,2)
            bot.send_document(message.chat.id, open(r'schedule.txt', 'r'))
        elif(message.text == '📝 вылет на весь день'):
            rqst.flight_table(event1,24)
            bot.send_document(message.chat.id, open(r'schedule.txt', 'r'))
            
        #-----железнодорожные рейсы-----#    
            
        elif message.text == "🚃 ж/д рейсы":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Московский")
            btn2 = types.KeyboardButton("Витебский")
            btn3 = types.KeyboardButton("Ладожский")
            btn4 = types.KeyboardButton("Балтийский")
            btn5 = types.KeyboardButton("Финляндский")
            back = types.KeyboardButton("🛑 Вернуться в главное меню") 
            markup.add(btn1, btn2, btn3, btn4, btn5, back)
            bot.send_message(message.chat.id, text= 'Выберете вокзал: ',reply_markup=markup)
            
        elif message.text == "Московский":
            markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn10 = types.KeyboardButton("🚉 отправление с Московского")
            btn20 = types.KeyboardButton("🚂 прибытие на Московский")
            back = types.KeyboardButton("🛑 Вернуться в главное меню") 
            markup1.add(btn10, btn20, back)
            bot.send_message(message.chat.id, text= 'Выберете time')
        elif message.text == "Витебский":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("🚉 отправление с Витебского")
            btn2 = types.KeyboardButton("🚂 прибытие на Витебский")
            back = types.KeyboardButton("🛑 Вернуться в главное меню") 
            markup.add(btn1, btn2, back)
        elif message.text == "Ладожский":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("🚉 отправление с Ладожского")
            btn2 = types.KeyboardButton("🚂 прибытие на Ладожский")
            back = types.KeyboardButton("🛑 Вернуться в главное меню") 
            markup.add(btn1, btn2, back)
        elif message.text == "Балтийский":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("🚉 отправление с Балтийского")
            btn2 = types.KeyboardButton("🚂 прибытие с Балтийского")
            back = types.KeyboardButton("🛑 Вернуться в главное меню") 
            markup.add(btn1, btn2, back)
        elif message.text == "Финляндский":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("🚉 отправление с Финляндского")
            btn2 = types.KeyboardButton("🚂 прибытие с Финляндского")
            back = types.KeyboardButton("🛑 Вернуться в главное меню") 
            markup.add(btn1, btn2, back)
        
        elif(message.text == '🚂 прибытие на Московский'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("💬 прибытие в ближайшие 2 часа на Московский")
            btn2 = types.KeyboardButton("📝 прибытие на весь день на Московский")
            back = types.KeyboardButton("🛑 Вернуться в главное меню") 
            markup.add(btn1, btn2, back)
            bot.send_message(message.chat.id, text = 'Выберете время приземление:',reply_markup=markup)
        
        elif(message.text == '🚉 отправление с Московского'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("💬 отправление 2 часа с Московского")
            btn2 = types.KeyboardButton("📝 отправление день с Московского")
            back = types.KeyboardButton("🛑 Вернуться в главное меню") 
            markup.add(btn1, btn2, back)
            bot.send_message(message.chat.id, text = 'Выберете время вылета:',reply_markup=markup)
        
        elif(message.text == '🚂 прибытие на Витебский'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("💬 прибытие в ближайшие 2 часа")
            btn2 = types.KeyboardButton("📝 прибытие на весь день")
            back = types.KeyboardButton("🛑 Вернуться в главное меню") 
            markup.add(btn1, btn2, back)
            bot.send_message(message.chat.id, text = 'Выберете время приземление:',reply_markup=markup)
        
        elif(message.text == '🚉 отправление с Витебского'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("💬 отправление в ближайшие 2 часа")
            btn2 = types.KeyboardButton("📝 отправление на весь день")
            back = types.KeyboardButton("🛑 Вернуться в главное меню") 
            markup.add(btn1, btn2, back)
            bot.send_message(message.chat.id, text = 'Выберете время вылета:',reply_markup=markup)
            
        elif(message.text == '🚂 прибытие на Ладожский'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("💬 прибытие в ближайшие 2 часа")
            btn2 = types.KeyboardButton("📝 прибытие на весь день")
            back = types.KeyboardButton("🛑 Вернуться в главное меню") 
            markup.add(btn1, btn2, back)
            bot.send_message(message.chat.id, text = 'Выберете время приземление:',reply_markup=markup)
        
        elif(message.text == '🚉 отправление с Ладожского'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("💬 отправление в ближайшие 2 часа")
            btn2 = types.KeyboardButton("📝 отправление на весь день")
            back = types.KeyboardButton("🛑 Вернуться в главное меню") 
            markup.add(btn1, btn2, back)
            bot.send_message(message.chat.id, text = 'Выберете время вылета:',reply_markup=markup)
        
        elif(message.text == '🚂 прибытие с Балтийского'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("💬 прибытие в ближайшие 2 часа")
            btn2 = types.KeyboardButton("📝 прибытие на весь день")
            back = types.KeyboardButton("🛑 Вернуться в главное меню") 
            markup.add(btn1, btn2, back)
            bot.send_message(message.chat.id, text = 'Выберете время приземление:',reply_markup=markup)
        
        elif(message.text == '🚉 отправление с Балтийского'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("💬 отправление в ближайшие 2 часа")
            btn2 = types.KeyboardButton("📝 отправление на весь день")
            back = types.KeyboardButton("🛑 Вернуться в главное меню") 
            markup.add(btn1, btn2, back)
            bot.send_message(message.chat.id, text = 'Выберете время вылета:',reply_markup=markup)
            
        elif(message.text == '🚂 прибытие с Финляндского'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("💬 прибытие в ближайшие 2 часа")
            btn2 = types.KeyboardButton("📝 прибытие на весь день")
            back = types.KeyboardButton("🛑 Вернуться в главное меню") 
            markup.add(btn1, btn2, back)
            bot.send_message(message.chat.id, text = 'Выберете время приземление:',reply_markup=markup)
        
        elif(message.text == '🚉 отправление с Финляндского'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("💬 отправление в ближайшие 2 часа")
            btn2 = types.KeyboardButton("📝 отправление на весь день")
            back = types.KeyboardButton("🛑 Вернуться в главное меню") 
            markup.add(btn1, btn2, back)
            bot.send_message(message.chat.id, text = 'Выберете время вылета:',reply_markup=markup)
            
            
        elif(message.text == '💬 прибытие в ближайшие 2 часа на Московский'):
            rqst.train_table('Moscow',event2,2)
            bot.send_document(message.chat.id, open(r'schedule.txt', 'r'))
        elif(message.text == '📝 прибытие на весь день на Московский'):
            rqst.train_table('Moscow',event2,24)
            bot.send_document(message.chat.id, open(r'schedule.txt', 'r'))
        elif(message.text == '💬 отправление 2 часа с Московского'):
            rqst.train_table('Moscow',event1,2)
            bot.send_document(message.chat.id, open(r'schedule.txt', 'r'))
        elif(message.text == '📝 отправление день с Московского'):
            rqst.train_table('Moscow',event1,24)
            bot.send_document(message.chat.id, open(r'schedule.txt', 'r'))
        
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