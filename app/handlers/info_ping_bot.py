from imaplib import Commands
import time
from aiogram import Router, types
from aiogram.types import Message
import logging

router = Router()

@router.message(commands = ["ping"], content_types = types.ContentType.GROUP_CHAT_CREATED)
async def cmd_ping(message: types.Message):
    for user in message.group_chat_created:
        await message.answer(f"name: 'erxdbot'\nyou:{user.fullname}")

