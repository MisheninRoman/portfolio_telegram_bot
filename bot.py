import asyncio
from aiogram import Bot, Dispatcher, types
from config import BOT_TOKEN
from handlers import handlers


async def main() -> None:
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(handlers.router)

    print("Бот запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
