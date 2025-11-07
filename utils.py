# utils.py

from database import Database
import datetime

# Создаем экземпляр базы данных для использования в utils
db = Database()


def get_daily_prediction(name, zodiac_sign):
    """
    Генерация полного предсказания на сегодня для конкретного знака зодиака.
    Гарантирует одинаковое предсказание в течение одного дня, но разное для разных знаков.
    """
    # Получаем сегодняшнюю дату в формате ГГГГ-ММ-ДД
    today = datetime.date.today()

    # Создаем "семя" для генерации псевдослучайного числа на основе даты и знака
    seed = f"{today}_{zodiac_sign}"

    # Получаем все предсказания для каждой категории
    actions = db.get_predictions_by_category("action")
    warnings = db.get_predictions_by_category("warning")
    advices = db.get_predictions_by_category("advice")

    # Генерируем индексы для каждой категории с использованием хеша
    # Добавляем имя категории к seed, чтобы индексы были разными для разных категорий
    action_idx = abs(hash(seed + "_action")) % len(actions)
    warning_idx = abs(hash(seed + "_warning")) % len(warnings)
    advice_idx = abs(hash(seed + "_advice")) % len(advices)

    # Получаем тексты предсказаний
    action_text = actions[action_idx]
    warning_text = warnings[warning_idx]
    advice_text = advices[advice_idx]

    # Формируем персонализированное сообщение
    return (
        f"{name}, вот ваше полное предсказание на сегодня:\n\n"
        f"Тебе сегодня нужно: {action_text}\n\n"
        f"Чего тебе нужно бояться: {warning_text}\n\n"
        f"Совет на день: {advice_text}"
    )