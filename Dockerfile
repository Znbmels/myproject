# Используем официальный образ Python 3.9-slim
FROM python:3.9-slim

# Устанавливаем системные зависимости, необходимые для сборки некоторых пакетов
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libssl-dev \
    python3-dev \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Обновляем pip до последней версии
RUN pip install --no-cache-dir --upgrade pip

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей в рабочую директорию
COPY requirements.txt /app/

# Устанавливаем Python-зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . /app/

# Открываем порт 8000 для доступа к приложению
EXPOSE 8000

# Запускаем сервер Django при старте контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
