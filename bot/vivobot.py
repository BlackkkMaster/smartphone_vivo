#!/usr/bin/python

import asyncio
import os
from random import randint

import dotenv
import telebot.async_telebot

from bot.utils import get_bool_env
from bot.vivopack import messages_pack

dotenv.load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

ADMIN_ID = os.getenv("ADMIN_ID", "909313568")
TARGET_USERS = os.getenv("TARGET_USER_IDS").split(",")
IS_ALLOW = get_bool_env(os.getenv("IS_ALLOW", "True"))

bot = telebot.async_telebot.AsyncTeleBot(API_TOKEN, "Markdown")


@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    try:
        if str(message.from_user.id) in TARGET_USERS and IS_ALLOW:
            await bot.reply_to(
                message,
                messages_pack[randint(1, len(messages_pack) - 1)],
            )
    except Exception as e:
        print(e)


asyncio.run(bot.polling())
