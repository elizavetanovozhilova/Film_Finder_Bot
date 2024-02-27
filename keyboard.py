from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, \
    KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu = [
    [InlineKeyboardButton(text="Узнать о фильме", callback_data="film_info"),
    InlineKeyboardButton(text="Подобрать фильм ", callback_data="find_film")],
    [InlineKeyboardButton(text="Рандомный фильм", callback_data="random_film")],
    [InlineKeyboardButton(text="🔎 Нужна помощь", callback_data="help")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Вернуться в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Вернуться в меню", callback_data="menu")]])
