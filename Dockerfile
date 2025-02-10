# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . .

# Собираем статические файлы
RUN python manage.py collectstatic --noinput

# Открываем порт
EXPOSE 8000

# Команда для запуска приложения
CMD ["gunicorn", "my_project.wsgi:application", "--bind", "0.0.0.0:8000"]
