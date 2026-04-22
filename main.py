import telebot

# بياناتك الخاصة
API_TOKEN = '8592913588:AAH7Miy67w6k8tmJ5_0siFx7GBmM-SpPMLA'
ADMIN_ID = 5957783780

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلاً بك! أرسل رسالتك وسأوصلها للمالك بسرية تامة.")

@bot.message_handler(func=lambda message: True)
def forward(message):
    user_info = f"👤 من: [{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    bot.send_message(ADMIN_ID, f"{user_info}\n\n📝 الرسالة:\n{message.text}", parse_mode="Markdown")
    bot.reply_to(message, "✅ تم إرسال رسالتك بنجاح!")

if __name__ == '__main__':
    bot.infinity_polling()
  
