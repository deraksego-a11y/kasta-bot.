import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart

# Безопасное получение токена
API_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(m: types.Message):
    await m.answer("Бот Kasta запущен через Koyeb!")

@dp.message(F.text)
async def txt(m: types.Message):
    await m.reply(f"Текст принят!")

@dp.message(F.photo)
async def img(m: types.Message):
    await m.reply("Фото сохранено!")

@dp.message(F.document)
async def doc(m: types.Message):
    if m.document.file_size > 70 * 1024 * 1024:
        await m.reply("Файл слишком большой (больше 70МБ)")
    else:
        await m.reply(f"Файл {m.document.file_name} получен!")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
