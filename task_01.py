"""
 Завдання 1
Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.
Вимоги до завдання:
Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
Для роботи з датами слід використовувати модуль datetime Python.
"""

from datetime import datetime


# Опис функції, що вона повинна зробити
def get_days_from_today(date):
    try:
        current_date = datetime.now()
        given_date = datetime.strptime(date, "%Y-%m-%d")
        result = given_date - current_date
        return result.days
    except (ValueError, TypeError) as error:
        print(f"Enter the date in the correct format\n YYYY-MM-DD")


# Виклик функції
if __name__ == "__main__":
    res = get_days_from_today("2024-04-30")  # 2
    print("res: ", res)
    res_2 = get_days_from_today("2024-04-01")  # -27
    print("res_2: ", res_2)
    res_3 = get_days_from_today("04-01-2024")  # None
    print("res_3: ", res_3)

