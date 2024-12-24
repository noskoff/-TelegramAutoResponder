import asyncio
from aiogram.utils import executor
from messages import dp

async def send_triggered_message():
    # Отправка сообщения по заранее заданному триггеру
    while True:
        # Здесь можно добавить любую логику для триггеров
        await asyncio.sleep(10)  # Отправлять раз в 10 секунд пример
        # Отправить сообщение всем пользователям, которые соответствуют триггеру
        # Для упрощения здесь нет обращения к базе данных
        user_id = 123456789  # Поменяйте на реальный идентификатор пользователя
        await dp.bot.send_message(user_id, "Это своеобразное уведомление по триггеру!")

async def main():
    # Запускаем задачи параллельно
    await asyncio.gather(
        send_triggered_message(),
        executor.start_polling(dp),
    )

if __name__ == '__main__':
    asyncio.run(main())
