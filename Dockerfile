# Базовый образ
FROM python:3.9-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Создание рабочей директории
WORKDIR /app

# Копирование зависимостей
COPY requirements.txt .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование остальных файлов проекта
COPY . .

# Сборка статических файлов
RUN python manage.py collectstatic --noinput

# Команда для запуска приложения
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]