import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from config import config
from Routers.main_router import main_router
from Routers.test_fsm import fsm_router
from Routers.json_router import json_router


logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()



async def main() -> None:

    await bot.delete_webhook(drop_pending_updates=True)

    dp.include_routers(
        main_router,
        fsm_router,
        json_router
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())