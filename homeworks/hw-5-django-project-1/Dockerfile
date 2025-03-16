FROM python:3.11-slim

WORKDIR /app

# Установка зависимостей системы
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Установка зависимостей Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование проекта
COPY . .

# Делаем wait-for-it.sh исполняемым
RUN chmod +x wait-for-it.sh

# Порт для Django
EXPOSE 8000

# Запуск через wait-for-it
CMD ["./wait-for-it.sh", "db", "python", "manage.py", "migrate", "&&", "python", "manage.py", "loaddata", "blog/fixtures/*.json", "&&", "python", "manage.py", "runserver", "0.0.0.0:8000"] 