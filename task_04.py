"""Завдання 4"""

from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    current_date = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=current_date.year)

        if birthday_this_year < current_date:
            birthday_this_year = birthday.replace(year=current_date.year + 1)

        delta_days = (birthday_this_year - current_date).days

        if delta_days < 7:
            # форматуємо дату у вигляді рядка
            formated_date = datetime.strftime(birthday_this_year, "%Y.%m.%d")

            # перевірка на вихідні дні
            if birthday_this_year.weekday() >= 5:
                days_until_monday = (7 - birthday_this_year.weekday()) % 7
                next_monday = birthday_this_year + timedelta(days=days_until_monday)
                formated_date = datetime.strftime(next_monday, "%Y.%m.%d")

            # додаємо словник із інформацією про день народження до списку привітань
            upcoming_birthdays.append(
                {
                    "name": user["name"],
                    "congratulation_date": formated_date,
                }
            )

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.04.30"},
    {"name": "Jane Smith", "birthday": "1990.05.02"},
    {"name": "Bill Gates", "birthday": "1990.05.04"},
    {"name": "Till Lindeman", "birthday": "1990.05.07"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print(upcoming_birthdays)
