from telebot import types
import telebot
bot = telebot.TeleBot('6906652701:AAE0SW7IkiIsXqgAVg4QY1tXbKO6Hr6b6SI')

greetings = """Hello! 👋 Welcome to our Telegram Clicker! 🚀

We’re excited to have you here. With our clicker, you can have fun and compete with your friends for the highest scores. 📈

Here’s what you can do:
- 🔥 Click and earn points
- 🏆 Compete with other players
- 🎁 Receive rewards for your achievements

Start right now! Hit the button and see how many points you can score. If you have any questions, just message us and we’ll help you out. 

Good luck and have fun! 😃

Let’s start clicking! 🎉"""

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()  # создаем inline клавиатуру
    key_launch = types.InlineKeyboardButton(text='Launch', callback_data='launch')  # создаем кнопку
    keyboard.add(key_launch)  # добавляем кнопку в клавиатуру
    key_community = types.InlineKeyboardButton(text='Join community', url="https://t.me/+Ff0ZFDVmcFsxYzli")  # создаем кнопку
    keyboard.add(key_community)  # добавляем кнопку в клавиатуру
    bot.send_message(message.chat.id, greetings, reply_markup=keyboard)  # отправляем сообщение с клавиатурой

@bot.callback_query_handler(func=lambda call: call.data == 'launch')
def handle(call):
    bot.send_message(call.message.chat.id, 'You clicked Launch!')

bot.polling(none_stop=True, interval=0)