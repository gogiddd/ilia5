from time import sleep
from pyrogram import Client, filters, types
from PIL import Image
import re
import asyncio

app = Client("session", api_id='29291003', api_hash='3de60c0bed05ae1fc504971139990843')


chat_id = "@anonkarubot"

@app.on_message(chat_id)
async def spam(client: Client, message: types.Message):
    if "/stop - завершить диалог" in message.text:  # Меняем это значение если хотим спамить в другом чате
        sleep(2.1)
        await app.send_message(chat_id, "Привет, трахнешь меня?")
        sleep(2.2)
        await app.send_message(chat_id, "Я недавно сняла видео с парнем , где он заполнил мне весь рот, посмотришь?)")

        if "/stop - завершить диалог" in message.text:
                sleep(2.3)
                await app.send_sticker(chat_id, "CAACAgIAAxkBAAEIIpVkEJEapUixeJdRi80B_Nl0dMilvQACuyEAAkqcwUopSnmOwlJlOS8E")
                sleep(2.4)

                if "/stop - завершить диалог" in message.text:  # Меняем это значение если хотим спамить в другом чате
                       await app.send_message(chat_id, "/stop")
                       sleep(2.5)
                       await app.send_message(chat_id, "/next")


app.run()

