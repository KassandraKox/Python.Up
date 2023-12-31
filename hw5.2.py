# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

names = ["John", "Jane", "James"]
salary = [500, 800, 1000]
kpi = ["10.25%", "15%", "17.5%"]
print({name: int(sal) / 100 * float(per[:-1]) for name, sal, per in zip(names, salary, kpi)})