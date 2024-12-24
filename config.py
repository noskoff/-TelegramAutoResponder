import os
from dotenv import load_dotenv

load_dotenv()

# Подключение к Telegram Bot API
API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

# Конфигурация базы данных PostgreSQL
DATABASE_CONFIG = {
    "host": os.getenv('DB_HOST', 'localhost'),
    "port": os.getenv('DB_PORT', '5432'),
    "user": os.getenv('DB_USER', 'postgres'),
    "password": os.getenv('DB_PASSWORD', 'password'),
    "database": os.getenv('DB_NAME', 'telegram_bot'),
}
