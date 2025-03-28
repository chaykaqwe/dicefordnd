from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from random import randint
import logging

import app.keybord as kb


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s",
    handlers=[
        logging.FileHandler("bot_logs.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)


router = Router(name=__name__)


@router.message(CommandStart())
async def comand_start(mes: Message):
    logging.info(f"Пользователь {mes.from_user.username} ({mes.from_user.id}) запустил бота.")
    await mes.answer_photo("https://ir.ozone.ru/s3/multimedia-t/c1000/6367003685.jpg",
                           caption='Добро пожаловать тут вы можите кидать кубики!', reply_markup=kb.main)


@router.message(F.text.startswith('d'))
async def rolldice(mes: Message):
    try:
        # Извлекаем число из команды, например dice6 → 6
        dice_size = int(mes.text.lstrip("d"))
        if dice_size < 2:  # Минимальный размер кубика - 2
            await mes.answer("Кубик должен иметь минимум 2 грани!")
            return

        # Генерируем случайное число
        result = randint(1, dice_size)

        # Определяем результат
        if result == dice_size:
            text = f"🎉 Критический успех! Выпало: {result}"
        elif result == 1:
            text = f"💀 Критический провал! Выпало: {result}"
        else:
            text = f"🎲 Ваше значение: {result}"

        await mes.answer(text)

    except ValueError:
        await mes.answer("Ошибка!   'Напишите фразу в формате dX, где X — количество граней кубика.")


@router.message(F.text == 'свое значение')
async def my_dice(mes: Message):
    await mes.answer('Напишите фразу в формате dX, где X — количество граней кубика.')


@router.message(F.text == 'Подбросить монету🪙')
async def my_dice(mes: Message):
    coin = randint(1, 2)
    if coin == 1:
        text = f'Орёл'
    else:
        text = f'Решка'
    await mes.answer(text)