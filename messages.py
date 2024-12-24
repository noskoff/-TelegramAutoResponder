from aiogram import Bot, Dispatcher, types
from aiogram.types.message import ContentType

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Функция для обработки любого текстового сообщения
@dp.message_handler(content_types=ContentType.TEXT)
async def handle_text_message(message: types.Message):
    if message.text.lower() in ["привет", "здравствуйте"]:
        await message.answer("Привет! Чем могу помочь?")
    elif "услуга" in message.text.lower():
        await message.answer("Мы предлагаем лучшие услуги! Напишите 'прайс', чтобы узнать цены.")
    else:
        await message.answer("Я вас понял! Напишите подробнее, пожалуйста.")
