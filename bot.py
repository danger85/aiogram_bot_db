import asyncio

import logging
import os #для token
import dotenv

from config_data.config import Config, load_config
from handlers import user_handlers, other_handlers
from keyboards.main_menu import set_main_menu

dotenv.load_dotenv()
Bot_Token=os.getenv("bot_token")
print(Bot_Token)

from aiogram import Bot, Dispatcher, F #
from aiogram.filters.command import Command # обработка команд
from aiogram.enums.dice_emoji import DiceEmoji # кубики подбрасывать
from aiogram import F # для обработки нажатий клавиш
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove,InlineKeyboardButton, CallbackQuery,InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

class CallBackParametrs(CallbackData,prefix='data'):
    keyboard:str
    value: str
    came_from: str

async def main():
  config: Config = load_config()

  # инициируем бота и диспетчер
  bot = Bot(token=config.tg_bot.token)
  dp = Dispatcher()

  #настраиваем главное меню бота
  await set_main_menu(bot)

  # регистируем роутеры в диспетчере
  dp.include_router(user_handlers.router)
  dp.include_router(other_handlers.router)

  # Пропускаем накопившиеся апдейты и запускаем polling
  await bot.delete_webhook(drop_pending_updates=True)
  await dp.start_polling(bot)

if __name__ == "__main__":
 asyncio.run(main())
