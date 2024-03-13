from aiogram import F, Router, types
from aiogram.types import Message
import keyboard
import text
router = Router()
from random import choice
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
import database

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(text.start.format(name=message.from_user.full_name), reply_markup=keyboard.menu)

@router.message(F.text.lower() == "меню")
@router.message(F.text.lower() == "выйти в меню")
@router.message(F.text == "◀️ Вернуться в меню")
async def menu(message: Message):
    await message.answer(text.menu, reply_markup=keyboard.menu)

@router.callback_query(F.data=='menu')
async def menuu(callback:types.callback_query):
    await callback.message.answer(text.menu, reply_markup=keyboard.menu)

films_dict={'barbie':'The film is about Barbie'}

class Form(StatesGroup):
    p=State()

@router.callback_query(StateFilter(None), F.data == "film_info")
async def film_info(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text.which_film)
    await state.set_state(Form.p)

@router.message(Form.p, F.text)
async def films_infoss(message: types.Message, state: FSMContext):
    await state.update_data(film=message.text)
    d=database.learn_about_film(message.text)
    await message.answer(d)
    await state.clear()


@router.callback_query(F.data == "random_film")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(f'{database.random_film()}')

@router.callback_query(F.data == "help")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(text.help_text, reply_markup=keyboard.iexit_kb)

@router.message(F.text)
async def random_text(message: types.Message):
    await message.answer(text.random_text, reply_markup=keyboard.menu)
