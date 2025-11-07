import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import commands, messages


async def main():
    """Основная функция запуска бота"""
    # Инициализируем бота с токеном
    bot = Bot(token=BOT_TOKEN)
    # Создаем диспетчер
    dp = Dispatcher()

    # Подключаем роутеры с обработчиками
    dp.include_router(commands.router)
    dp.include_router(messages.router)

    # Запускаем бота в режиме опроса обновлений
    await dp.start_polling(bot)


if __name__ == "__main__":
    # Запускаем асинхронную функцию main()
    asyncio.run(main())