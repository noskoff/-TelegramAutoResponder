from aiogram import types
from messages import handle_text_message
import pytest

@pytest.mark.asyncio
async def test_handle_text_message():
    message = types.Message(text='привет', from_user=types.User(id=1, is_bot=False))
    await handle_text_message(message)
    # Пример проверки ответа: здесь должна быть имитация ответа на сообщение
    assert message.text == "Привет! Чем могу помочь?"  # Перепроверьте реальную отправку
