"""
 Завдання 2
Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали випадковим чином і в певному діапазоні під час чергового тиражу. Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей. Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.
"""

import random


def get_numbers_ticket(min, max, quantity):
    numbers_1 = random.sample(range(min, max), quantity)
    return numbers_1


# lottery_numbers_1 = get_numbers_ticket(1, 50, 6)
# print("Ваші лотерейні числа:", lottery_numbers_1)
# lottery_numbers_2 = get_numbers_ticket(100, 137, 5)
# print("Ваші лотерейні числа:", lottery_numbers_2)
# lottery_numbers_3 = get_numbers_ticket(200, 300, 3)
# print("Ваші лотерейні числа:", lottery_numbers_3)
