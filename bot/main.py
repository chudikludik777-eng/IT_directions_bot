import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from config import BOT_TOKEN
from handlers.start import router as start_router
from handlers.main import router as main_router


load_dotenv()


async def main():
    if not BOT_TOKEN:
        raise ValueError("Токен не нейден. Убедитесь, что переменная окружения TOKEN установлена.")
    dp = Dispatcher()
    bot = Bot(token=BOT_TOKEN)
    dp.include_router(start_router)
    dp.include_router(main_router)
    print("Bot Started ✅")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
