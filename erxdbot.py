import asyncio
import logging
from aiogram import Bot, Dispatcher, types, Router
from app.config import TOKEN, TG_ID
from app.handlers import dice, cards, info_ping_bot

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    dp.include_router(dice.router)
    dp.include_router(cards.router)
    dp.include_router(info_ping_bot.router)

    @dp.message(commands=["start"])
    async def cmd_start(message: types.Message):
        await message.answer("Привет!\nЭтот бот создан для помощи в группах.\nНапиши комманду /help , чтобы узнать подробнее")

    @dp.message(commands=["help"])
    async def start_helper(message: types.Message):
        await message.answer(
            "Что умеет этот бот:\nбаскетбол - /basket, /b_dice\nподбросить кость - /dice, /cube"
            )

    @dp.message(content_types=types.ContentType.NEW_CHAT_MEMBERS)
    async def somebody_added(message: types.Message):
        for user in message.new_chat_members:
            await message.reply(f"Привет, {user.full_name}")

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot) 
'''
@dp.message(content_types="text")
async def extract_data(message: types.Message):
    data = {
        "url": "<N/A>",
        "email": "<N/A>",
        "code": "<N/A>"
    }
    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            # Неправильно
            # data[item.type] = message.text[item.offset : item.offset+item.length]
            # Правильно
            data[item.type] = item.extract(message.text)
    await message.reply(
        "Вот что я нашёл:\n"
        f"URL: {html.quote(data['url'])}\n"
        f"E-mail: {html.quote(data['email'])}\n"
        f"Пароль: {html.quote(data['code'])}"
    )

@dp.message(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def somebody_added(message: types.Message):
    for user in message.new_chat_members:
        # проперти full_name берёт сразу имя И фамилию 
        # (на скриншоте выше у юзеров нет фамилии)
        await message.reply(f"Привет, {user.full_name}")

from aiogram.utils.keyboard import ReplyKeyboardBuilder


@dp.message(commands=["dice"])
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")
'''
if __name__ == "__main__":
    asyncio.run(main())
    
