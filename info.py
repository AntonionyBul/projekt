from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, Updater
from bs4 import BeautifulSoup
import random
import requests


def get_gif():
    url = "https://tenor.com/ru/search/cats-gifs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    gifs = soup.select("img[src*='https://media.tenor.com/']")
    random_gif = random.choice(gifs)
    gif_url = random_gif["src"]
    return gif_url


def generator(a):
    s1 = "y"
    for j in range(a):
        for i in range(random.randint(1, 2)):
            s1 = s1 + " y"
        b = random.randint(0, 5)
        if (b == 0):
            c = random.randint(0, 2)
            if (c == 0):
                s1 = s1 + " -"
            else:
                s1 = s1 + ","
        elif (b == 1):
            c = random.randint(0, 3)
            if (c == 0):
                s1 = s1 + ". x"
            elif (c == 1):
                s1 = s1 + "! x"
            else:
                s1 = s1 + "? x"
        elif (b == 3):
            s1 = s1 + ":"
            for x in range(random.randint(1, 4)):
                for z in range(random.randint(1, 3)):
                    s1 = s1 + " y"
                s1 = s1 + ","
            for i in range(random.randint(1, 2)):
                s1 = s1 + " y"
            s1 = s1 + ". x"
        else:
            for w in range(random.randint(0, 3)):
                s1 = s1 + " y"
        q = random.randint(0, 2)

        if (s1[-1] != ",") and (q != 0) and (s1[-1] != "-"):
            s1 = s1 + "," + " y"
    return (s1)


def get_meow():
    ss = generator(3)
    ss = "x " + ss + " y"
    v = random.randint(0, 2)
    if (v == 0):
        ss = ss + "."
    elif (v == 1):
        ss = ss + "!"
    else:
        ss = ss + "?"
    ss = ss.replace("x", "Meow")
    ss = ss.replace("y", "meow")
    return ss


def text_gif_callback(update, context):
    chat_id = update.callback_query.message.chat_id
    url = get_gif()
    context.bot.send_video(chat_id, url, 'None')
    context.bot.send_message(chat_id=chat_id, text=get_meow())


def start_command(update, context):
    chat_id = update.message.chat_id
    keyboard = [[InlineKeyboardButton("Гифка", callback_data='gif')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(
        chat_id=chat_id, text="Привет! Хочешь гифку с котиками?", reply_markup=reply_markup)


updater = Updater(token='6144493620:AAGyR7wphldUMMD3rIxbz1oD3xLRogNCzsA', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start_command))
dispatcher.add_handler(CallbackQueryHandler(
    text_gif_callback, pattern='gif'))

updater.start_polling()
