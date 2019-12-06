import telebot
from random import randint

bot = telebot.TeleBot('1040628806:AAHLkb6i6BhQCVQq81bIJabXMRelXJ3vEKk')

startMessage = f'''Этот бот генерирует рандомные числа.
Просто введи через пробел два числа, в диапозоне которых и будет сгенерировано число.
Для полной информации используй /help'''

helpMessage = f'''Напиши /start Для вывода приветственного сообщения
Напиши /help Для помощи

Это программа генерирует рандомные числа
Для ответа, напишите через пробел 2 натуральных числа
Например: 2 33. Теперь вы задали диапозон от 2 до 33
Теперь бот напишет вам сообщение с ответом
Если хотите, чтобы от в том же диапозоне выдал ещё один результат, то нажмите: Ещё раз
Если хотите изменить диапозон, то просто введите 2 новые числа
'''

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Ещё раз')

a = 0
b = 0

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'Привет, {message.chat.first_name}.\n' + startMessage, reply_markup=keyboard1)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, helpMessage)

@bot.message_handler(content_types=['text'])
def send_text(message):
    global a, b
    if message.text.lower() == 'ещё раз':
        bot.send_message(message.chat.id, f'В диапозоне от {a} до {b}\nСгенерирвано: {randint(a, b)}')
    else:
        a = ''
        b = ''
        for i in range(0, len(message.text) - 1):
            if message.text[i] != ' ':
                a = str(a)
                a += message.text[i]
                a = int(a)
            else:
                for k in range(i + 1, len(message.text)):
                    b = str(b)
                    b += message.text[k]
                    b = int(b)
                break
        bot.send_message(message.chat.id, f'В диапозоне от {a} до {b}\nСгенерирвано: {randint(a, b)}')

bot.polling()
