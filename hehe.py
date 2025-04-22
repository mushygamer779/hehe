from telebot import TeleBot
import random, os, func

bot = TeleBot('7604409864:AAHUpDELo8wSGNuqgPS9XskyVk0EsGWagTA')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'this bot is made to tell you how to throw stuff away use /throw_away and what you want to throw away')



@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, 'use /throw_away to know how to throw away certain stuff use dont_throw to see what happens to the surroundings if you throw a  certain thing in trash use daily_quest to know your daily quests and daily quest complete to show that you completed the quest')



@bot.message_handler(commands=['throw_away'])
def start(message):
    try:
        mes = message.text.split()
        if mes[1] == 'batteries':
            bot.reply_to(message, 'here are places of places that recycle batteries: https://www.google.com.tr/maps/search/recycle+batteries/@31.1673472,8.8444377,3z?entry=ttu&g_ep=EgoyMDI1MDQxNi4xIKXMDSoASAFQAw%3D%3D')
        elif mes[2] == 'home lamp':
            bot.reply_to(message, 'first disassemble the lamp recycly the battery and put everything else in a bag')     
       
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
        '''elif mes_2[1] == 'home lamp':
            bot.reply_to(message, 'this is what happens when you dont properly throw away home lapms')
            with open('photos//' + random.choice(os.listdir('photos')), 'rb') as f:  
                bot.send_photo(message.chat.id, f) '''
    
    except:
        bot.reply_to(message, 'it has to be dont_throw and the thing you want to throw through space')     



bot.infinity_polling()
