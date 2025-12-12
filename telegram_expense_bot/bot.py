import os
from telebot import TeleBot
from utils.storage import add_expense, get_total, get_all, reset_data


TOKEN = os.getenv("BOT_TOKEN") # token is read from environment variable
bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
bot.reply_to(message, "Hi! I'm your expense tracker.
"
"Add an expense: /add 120 food
"
"See total: /total
"
"List all: /list")


@bot.message_handler(commands=['add'])
def add(message):
try:
# expects: /add <amount> <category>
_, amount, category = message.text.split(maxsplit=2)
amount = float(amount)
add_expense(amount, category)
bot.reply_to(message, f"Added: {amount} ({category})")
except Exception:
bot.reply_to(message, "Usage: /add 150 food")


@bot.message_handler(commands=['total'])
def total(message):
bot.reply_to(message, f"Monthly total: {get_total()}")


@bot.message_handler(commands=['list'])
def list_expenses(message):
data = get_all()
if not data:
bot.reply_to(message, "No expenses recorded yet.")
else:
text = "
".join([f"{i+1}. {item['amount']} — {item['category']}" for i, item in enumerate(data)])
bot.reply_to(message, text)


@bot.message_handler(commands=['reset'])
def reset(message):
reset_data()
bot.reply_to(message, "Data cleared!")


if __name__ == '__main__':
bot.polling()