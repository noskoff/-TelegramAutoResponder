# Используем Python 3.10
FROM python:3.10

# Рабочая директория в контейнере
WORKDIR /app

# Копируем все файлы в контейнер
COPY . /app

# Установка зависимостей
RUN pip install -r requirements.txt

# Команда для запуска бота
CMD ["python", "main.py"]
