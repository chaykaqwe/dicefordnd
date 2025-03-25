import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.hundlers import router


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
