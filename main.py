import telebot
from telebot import types
import multiprocessing
import os
from flask import Flask

# --- إعدادات المالك ---
API_TOKEN = '8592913588:AAG7mFWiNveb68lO53q_ICJEa8LibEgcQwE'
OWNER_ID = 5957783780
bot = telebot.TeleBot(API_TOKEN)

# إعداد PORT لـ Render
PORT = int(os.environ.get('PORT', 8080))
user_states = {}

# --- دالة تشغيل البوتات الفرعية ---
def run_sub_bot(token, b_type):
    try:
        sub_bot = telebot.TeleBot(token)
        @sub_bot.message_handler(commands=['start'])
        def start(m):
            sub_bot.reply_to(m, f"✅ أهلاً بك! هذا بوت {b_type} تم إنشاؤه عبر المصنع.")
        sub_bot.infinity_polling()
    except:
        pass

# --- أزرار التحكم ---
def start_markup():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add("1- صارحني 💌", "2- حماية كروبات 🛡️", "3- اشتراك اجباري 📢", "4- بوتات إحالة 👥", "5- بوت سايت 🌐")
    return markup

@bot.message_handler(commands=['start'])
def main_start(message):
    bot.send_message(message.chat.id, "مرحباً بك في صانع البوتات الاحترافي 🗿🔥\nاختر نوع البوت الذي تريد إنشاءه:", reply_markup=start_markup())

@bot.message_handler(func=lambda m: True)
def handle_msg(message):
    if any(x in message.text for x in ["1-", "2-", "3-", "4-", "5-"]):
        user_states[message.chat.id] = message.text
        bot.send_message(message.chat.id, f"ممتاز، اخترت {message.text}.\nالآن أرسل 'توكن' البوت من @BotFather:")
    elif ":" in message.text:
        b_type = user_states.get(message.chat.id, "عام")
        bot.send_message(message.chat.id, "🚀 جاري تشغيل بوتك... انتظر لحظة.")
        multiprocessing.Process(target=run_sub_bot, args=(message.text, b_type)).start()
        bot.send_message(message.chat.id, "✅ مبروك! بوتك يعمل الآن.")

# --- تشغيل السيرفر والبوت ---
app = Flask(__name__)
@app.route('/')
def index(): return "Factory Online"

if __name__ == '__main__':
    multiprocessing.Process(target=lambda: bot.infinity_polling()).start()
    app.run(host='0.0.0.0', port=PORT)
