import telebot

# Замените 'YOUR_BOT_TOKEN' на токен, который вы получили от BotFather
TOKEN = '6995120433:AAE8nfu9jCKQ3ASQVM6vddDrKqdv39cO2E0'
bot = telebot.TeleBot(TOKEN)

# Обработчик для текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, 'Я нахожусь в процессе разработки.')

# Запускаем бота
bot.polling()

