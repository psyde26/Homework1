from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
from datetime import date, datetime


PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = "Вызван /start. Только зачем?"
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = 'Привет, {}! Ты написал: {}.'.format(update.message.chat.first_name, update.message.text)
    logging.info('User: %s, ChatID: %s, Message: %s', update.message.chat.username,
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def planet_info(bot, update):
    user_answer = (update.message.text).split(' ')
    print(user_answer[1])
    time_now = ephem.Date(datetime.now())
    (print(time_now))
    planet_dicts = {
                'Mercury': ephem.constellation(ephem.Mercury(time_now)), 'Venus': ephem.constellation(ephem.Venus(time_now)),
                'Mars': ephem.constellation(ephem.Mars(time_now)), 
                'Jupiter': ephem.constellation(ephem.Jupiter(time_now)), 'Saturn': ephem.constellation(ephem.Saturn(time_now)),
                'Uranus': ephem.constellation(ephem.Uranus(time_now)), 'Neptune': ephem.constellation(ephem.Neptune(time_now))
                 }
    if user_answer[1] in planet_dicts:
        result = planet_dicts.get(user_answer[1])
    else:
        result = 'А вот и нет такой планеты, {}'.format(update.message.chat.first_name)
    
    update.message.reply_text(result)
    

def main():
    mybot = Updater("829589905:AAF9N81vkiZviIV9gIk4P2Af9-lq9vHlBY0", request_kwargs=PROXY)
    
    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler('planet', planet_info))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


main()