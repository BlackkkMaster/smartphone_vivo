#!/usr/bin/python

import asyncio
import os
from random import randint

import dotenv
import telebot.async_telebot
import utils
import vivopack

dotenv.load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

ADMIN_ID = os.getenv("ADMIN_ID", "909313568")
TARGET_USERS = os.getenv("TARGET_USER_IDS", "1117090847").split(",")
IS_ALLOW = utils.get_bool_env(os.getenv("IS_ALLOW", "True"))

vibot = telebot.async_telebot.AsyncTeleBot(API_TOKEN, "Markdown")


@vibot.message_handler(
    func=lambda message: True,
    content_types=[
        "text",
        "animation",
        "audio",
        "document",
        "photo",
        "sticker",
        "story",
        "video",
        "video_note",
        "voice",
        "contact",
        "dice",
        "game",
        "poll",
        "venue",
        "location",
        "invoice",
        "successful_payment",
        "connected_website",
        "passport_data",
        "web_app_data",
    ],
)
async def echo_message(message):
    try:
        if str(message.from_user.id) in TARGET_USERS and IS_ALLOW:
            await vibot.reply_to(
                message,
                vivopack.messages_pack[
                    randint(0, len(vivopack.messages_pack) - 1)
                ],
            )
    except Exception as e:
        print(e)


asyncio.run(vibot.polling())
