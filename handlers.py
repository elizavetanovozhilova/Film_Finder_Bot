from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message
import keyboard
import text
router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(text.start.format(name=message.from_user.full_name), reply_markup=keyboard.menu)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(message: Message):
    await message.answer(text.menu, reply_markup=keyboard.menu)
