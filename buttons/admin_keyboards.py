from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


Menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add('Каталог', 'Корзина', 'Контакты', 'Админ панель')

adminMenu = ReplyKeyboardMarkup(resize_keyboard=True).add('Добавить товар', 'Удалить товар')


