import os
import telebot
from flask import Flask
from threading import Thread

TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route("/")
def home():
    return "Angishvona AI Scanner ishlayapti!"

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "🎯 Angishvona AI Scanner botiga xush kelibsiz!\n\n"
        "O‘yin videosini yuboring. AI tahlil qiladi."
    )

@bot.message_handler(content_types=["video"])
def video(message):
    bot.reply_to(
        message,
        "🎥 Video qabul qilindi!\n"
        "🔍 Tahlilga tayyorlanmoqda..."
    )

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    Thread(target=run_bot, daemon=True).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
