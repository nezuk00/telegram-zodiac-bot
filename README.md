# Учебный Telegram-бот

Команды, клавиатура со знаками зодиака и предсказания из SQLite. Требует настройки и проверки запуска.

**Стек:** Python, aiogram, SQLite.

Учебный проект: лабораторная работа или практика. Описание составлено по исходникам; повторный запуск всех заданий и моделей не выполнялся.

## Содержимое

| Файл / папка | Назначение |
| --- | --- |
| [bot.py](https://github.com/nezuk00/telegram-zodiac-bot/tree/master/bot.py) | Файл проекта |
| [config.py](https://github.com/nezuk00/telegram-zodiac-bot/tree/master/config.py) | Файл проекта |
| [database.py](https://github.com/nezuk00/telegram-zodiac-bot/tree/master/database.py) | Файл проекта |
| [handlers](https://github.com/nezuk00/telegram-zodiac-bot/tree/master/handlers) | Исходники / материалы |
| [keyboards.py](https://github.com/nezuk00/telegram-zodiac-bot/tree/master/keyboards.py) | Файл проекта |
| [requirements.txt](https://github.com/nezuk00/telegram-zodiac-bot/tree/master/requirements.txt) | Файл проекта |
| [utils.py](https://github.com/nezuk00/telegram-zodiac-bot/tree/master/utils.py) | Файл проекта |

## Как изучить

Начните с исходников и файлов зависимостей в этом репозитории. Учебные скрипты могут ожидать пользовательский ввод или локальные файлы.

[Другие учебные работы и проекты](https://github.com/nezuk00)

## Перед запуском

Токен, ранее попавший в историю Git, необходимо отозвать через BotFather и заменить локально. Текущее значение удалено из .env. Также в bot.py после start_polling присутствует лишний текст `git add .`, который нужно убрать перед запуском. Этот репозиторий описывает учебную работу и не заявлен как готовый сервис.
