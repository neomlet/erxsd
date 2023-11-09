import time
from aiogram import Router, types
from aiogram.types import Message, Dice
from aiogram.methods.send_dice import SendDice

router = Router()

@router.message(commands=["basketball", "b_dice", "basket", "basketdice"])
async def cmd_BASKETBALL(message: types.Message):
    #await message.answer_dice(emoji="🏀")
    msg = await message.answer_dice(emoji="🏀")
    qwer = msg.dice.value
    print(qwer)
    if qwer >3:
        time.sleep(5)
        await message.answer("люти")
    else:
        time.sleep(5)
        await message.answer("лошара ебаная")

@router.message(commands=["dice", "cube", "cub", "six", "c_dice"])
async def cmd_dice(message: types.Message):
    qwe = await message.answer_dice(emoji="🎲")
    dfg = qwe.dice.value
    time.sleep(5)
    await message.answer(f"Вам выпало число: {dfg}")

@router.message(commands=["dart"])
async def cmd_dart(message: types.Message):
    await message.answer_dice(emoji="🎯")

@router.message(commands=["bowling"])
async def cmd_BOWLING(message: types.Message):
    await message.answer_dice(emoji="🎳")

@router.message(commands=["slot"])
async def cmd_slot(message: types.Message):
    await message.answer_dice(emoji="🎰")