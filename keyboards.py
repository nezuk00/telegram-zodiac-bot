# keyboards.py

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_zodiac_keyboard():
    """Создание клавиатуры со знаками зодиака и кнопкой для получения предсказания"""
    zodiac_signs = [
        'Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева',
        'Весы', 'Скорпион', 'Стрелец', 'Козерог', 'Водолей', 'Рыбы'
    ]

    # Создаем кнопки в формате 3x4
    buttons = []
    for i in range(0, len(zodiac_signs), 3):
        row = zodiac_signs[i:i + 3]
        buttons.append([KeyboardButton(text=sign) for sign in row])

    # Добавляем кнопку "Посмотреть предсказание на сегодня"
    buttons.append([KeyboardButton(text="Посмотреть предсказание на сегодня")])

    # Возвращаем клавиатуру
    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        one_time_keyboard=False  # Клавиатура остается после нажатия
    )