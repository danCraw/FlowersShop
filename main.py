from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, MenuButton
from aiogram.utils import executor
from fastapi import FastAPI
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from constants import START_TEXT, SELECT_TEXT
from mimesis import Person, Text
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{'postgres'}:{'postgres'}@{'localhost'}:5432/{'flowers_shop'}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

# берем параметры БД из переменных окружения
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_HOST = "localhost"
DB_NAME = "special"
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{'postgres'}:{'postgres'}@{'localhost'}:5432/{'flowers_shop'}"
)

# создаем объект database, который будет использоваться для выполнения запросов
db = SQLAlchemy(app)

person = Person('ru')
text = Text('ru')
bot = Bot(token='5738149394:AAF9EbU3IBT0-6MoayLDUNgDTIsCySL8VuE')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    b = MenuButton()
    await bot.set_chat_menu_button(chat_id=message.from_user.id, menu_button=b)
    await bot.send_message(chat_id=message.from_user.id, text="<b>Что умеет этот бот?</b>\nПродажа цветов\n<b>Жми начать!</b>",
                           parse_mode='html', reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(START_TEXT)]], resize_keyboard=True))


@dp.message_handler(lambda message: message.text and 'hello' in message.text.lower())
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


@dp.message_handler(lambda message: message.text and START_TEXT in message.text.lower())
async def process_begin_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="<b>Приветственное сообщение</b>\nНе забудьте прочитать описание!\n", parse_mode='html')
    await bot.send_message(chat_id=message.from_user.id, text="<b>Выберите по фотографии</b>\nНе забудьте прочитать описание!\nВы можете написать в техподдержку мы попытаемся вам помочь\n",
                           parse_mode='html', reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(SELECT_TEXT)]], resize_keyboard=True))


if __name__ == '__main__':
    print('Запущен')
    executor.start_polling(dp)
    print('Остановлен')