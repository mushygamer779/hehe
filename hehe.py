from telebot import TeleBot
import random, os

bot = TeleBot('7604409864:AAHUpDELo8wSGNuqgPS9XskyVk0EsGWagTA')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'this bot is made to tell you how to throw stuff away use /hw.tu and what you want to throw away')
    
@bot.message_handler(commands=['throw_away'])
def start(message):
    try:
        mes = message.text.split()
        if mes[1] == 'batteries':
            bot.reply_to(message, 'here are places of places that recycle batteries: https://www.google.com.tr/maps/search/recycle+batteries/@31.1673472,8.8444377,3z?entry=ttu&g_ep=EgoyMDI1MDQxNi4xIKXMDSoASAFQAw%3D%3D')
        '''elif mes[2] == 'home lamp':
            bot.reply_to(message, 'fir')   '''             
    except:
        bot.reply_to(message, 'it has to be throw_away and the thing you want to throw through space')


@bot.message_handler(commands=['dont_throw'])
def start(message):
    try:
        mes_2 = message.text.split()
        if mes_2[1] == 'batteries':
            bot.reply_to(message, 'this is what happens when you dont recycle batteries')
            with open('photos//' + random.choice(os.listdir('photos')), 'rb') as f:  
                bot.send_photo(message.chat.id, f) 
    
    except:
        bot.reply_to(message, 'it has to be dont_throw and the thing you want to throw through space')     



bot.infinity_polling()
