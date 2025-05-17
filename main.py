import telebot
import time
import random

API_TOKEN = '8111113527:AAENybSg6CZEnYrtjGC1Mlo78T5XSrJ4qIQ'
GROUP_CHAT_ID = '@wavytushar'  # Telegram group or channel

bot = telebot.TeleBot(API_TOKEN)
signal_running = False

pairs = ['EUR/USD', 'GBP/JPY', 'AUD/USD', 'USD/JPY', 'EUR/JPY']
directions = ['CALL', 'PUT']

def generate_signal():
    pair = random.choice(pairs)
    direction = random.choice(directions)
    return f"💹 Signal:\nPair: {pair}\nDirection: {direction}\nTime: 1 minute"

@bot.message_handler(commands=['startsignals'])
def start_signals(message):
    global signal_running
    if not signal_running:
        signal_running = True
        bot.reply_to(message, "✅ Signals started.")
        while signal_running:
            signal = generate_signal()
            bot.send_message(GROUP_CHAT_ID, signal)
            time.sleep(60)
            result = random.choice(["✅ WIN", "❌ LOSS"])
            bot.send_message(GROUP_CHAT_ID, f"📊 Result: {result}")
            time.sleep(5)
    else:
        bot.reply_to(message, "🚨 Signals already running.")

@bot.message_handler(commands=['stopsignals'])
def stop_signals(message):
    global signal_running
    signal_running = False
    bot.reply_to(message, "🛑 Signals stopped.")

bot.polling()
