# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /hw1

# Копируем все файлы и папки из hw1 в образ
COPY . .

# Устанавливаем необходимые зависимости (если есть requirements.txt)
# RUN pip install --no-cache-dir -r requirements.txt

# Запускаем Python-скрипт
CMD ["python", "main.py"]