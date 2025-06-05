from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

API_TOKEN = '7977201566:AAHan0eTiZV4ysjmGhM4uevvLcTw4qOuqfk'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton("Играть", web_app=WebAppInfo(url="https://butontapgame.vercel.app"))
)

@dp.message_handler(commands=['start'])
async def start_game(message: types.Message):
    await message.answer("Запусти игру прямо в Telegram 👇", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
