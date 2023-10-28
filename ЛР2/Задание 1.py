money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month = 0 # счётчик месяцев
budjet = money_capital + salary # бюджет на первый месяц
expenses = spend # счётчик затрат
result = budjet - expenses # бюджет по истечению первого месяца
while result > 0:
    expenses += expenses * increase
    result -= expenses
    result += salary
    month += 1# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", month)
