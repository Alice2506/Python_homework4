# 1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

from sys import argv

script, working_hours_amount, hour_wage_rate, bonus = argv

def get_salary(working_hours_amount, hour_wage_rate, bonus):
    salary = working_hours_amount * hour_wage_rate + bonus
    return salary

print(get_salary(int(working_hours_amount), int(hour_wage_rate), int(bonus)))



