from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
from data.config import config_file

storage = MemoryStorage()
bot = Bot(config_file['token'])
dp = Dispatcher(bot, storage=storage)