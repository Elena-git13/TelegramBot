import telebot

# 1878344485:AAH8a2f4rXJ8-YrveKa_jcwbuFDdhQwJp-U

name = ''
surname = ''
age = 0
work = ''

bot = telebot.TeleBot("1878344485:AAH8a2f4rXJ8-YrveKa_jcwbuFDdhQwJp-U")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'Привет!':
        bot.reply_to(message, 'Привет,как дела?')
    elif message.text == 'Hi!':
        bot.reply_to(message, 'Hi! How are you?')
    elif message.text == '/reg':
        bot.send_message(message.from_user.id, 'Привет! Как тебя зовут?')
        bot.register_next_step_handler(message, reg_name)
	#bot.reply_to(message, message.text)

def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, reg_surname)

def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'В какой компании ты работаешь?')
    bot.register_next_step_handler(message, reg_work)

def reg_work(message):
    global work
    work = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, reg_age)

def reg_age(message):
    global age
    #age = message.text
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Вводите цыфрами')

bot.polling()
