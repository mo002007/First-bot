import telebot
from telebot import types
import os
from flask import Flask
from threading import Thread

# --- إعداداتك ---
TOKEN = '8592913588:AAG7mFWiNveb68lO53q_ICJEa8LibEgcQwE'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home(): return "Bot is Running"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("1- صارحني 💌", "2- حماية 🛡️", "3- إحالة 👥")
    bot.send_message(message.chat.id, "🔥 أهلاً بك في مصنع البوتات\nاختر نوع البوت:", reply_markup=markup)

if __name__ == "__main__":
    # تشغيل سيرفر الويب في خلفية منفصلة لتجنب Error 1
    Thread(target=run_flask).start()
    print("🚀 Bot is starting...")
    bot.infinity_polling()
