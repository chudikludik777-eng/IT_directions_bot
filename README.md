# Telegram IT Bot

Простой Telegram-бот на aiogram, который рассказывает про IT-направления и помогает новичкам начать путь.

---

## Требования

- Python 3.10+
- Telegram Bot Token (через @BotFather)


---

## Установка и запуск

### 1. Клонировать репозиторий
```bash
https://github.com/chudikludik777-eng/IT_directions_bot.git

2. Создать виртуальное окружение
python -m venv venv

Windows
venv\Scripts\activate

Linux / macOS
source venv/bin/activate

3. Установить зависимости
pip install aiogram

Настройка бота
4. Создать бота в Telegram
Открыть @BotFather

Создать бота (/newbot)

Скопировать BOT TOKEN

5. Указать токен
Создаешь новую папку под именем .env и дальше

TOKEN=""
⚠️ внутри пишешь только токен

Запуск
python main.py
После запуска открыть Telegram и написать боту:

/start
