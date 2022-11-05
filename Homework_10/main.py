import telebot 
from telebot import types
from logger import *

bot = telebot.TeleBot("5620208452:AAFgnS7aCl0xg3izV_fBjnnbECrERL6VUzI")

result = ''

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "🤖 \nЯ бот - Калькулятор")
        bot.send_message(message.from_user.id, "Напиши операцию, которую необходимо вычислить")
        bot.register_next_step_handler(message, calc_command)
        info_logger(f'{message.from_user.username} /start')
    else:
        bot.send_message(message.from_user.id, 'Напиши /start')


def calc_command(message):
    try:
        global result
        user_value = message.text
        result = eval(str(user_value))
        info_logger(f'Запрос обработан: {message.from_user.username} {user_value} = {result}')
        answer = f'{user_value} = {result}'
        bot.send_message(message.from_user.id, answer)
    except NameError:
        info_logger(f'Ошибка NameError: {message.from_user.username} {user_value}')
        bot.send_message(message.from_user.id, '❗ Некорректный ввод. \nКалькулятор работает только с цифрами.')
        bot.send_message(message.from_user.id, "Напиши операцию, которую необходимо вычислить")
        bot.register_next_step_handler(message, calc_command)
    except TypeError:
        info_logger(f'Ошибка TypeError: {message.from_user.username} {user_value}')
        bot.send_message(message.from_user.id, '❗ Некорректный ввод. \nВозможно, не все знаки.')
        bot.send_message(message.from_user.id, "Напиши операцию, которую необходимо вычислить")
        bot.register_next_step_handler(message, calc_command)
    except:
        info_logger(f'Ошибка: {message.from_user.username} {user_value}')
        bot.send_message(message.from_user.id, '💔 Что-то пошло не так... \nДавай попробуем еще раз')
        bot.send_message(message.from_user.id, "Напиши операцию, которую необходимо вычислить")


bot.polling(none_stop=True, interval=0)
