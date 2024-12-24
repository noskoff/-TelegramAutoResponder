import asyncio
from aiogram import Bot
from config import API_TOKEN

bot = Bot(token=API_TOKEN)

async def scheduled_broadcast():
    # Пример отправки сообщений по расписанию
    while True:
        await asyncio.sleep(86400)  # Раз в день
        user_ids = [123456789, 987654321]  # Заглушка: замените на реальные ID
        for user_id in user_ids:
            await bot.send_message(user_id, "Добро пожаловать в наш клуб!")
