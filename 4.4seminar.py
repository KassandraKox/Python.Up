# Функция принимает на вход три списка одинаковой длины:
# имена str,
# ставка int,
# премия str с указанием процентов вида «10.25%».
# Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.
def calculate_salary(personal):
    return {name: int(sal) / 100 * float(per[:-1]) for name, sal, per in personal}


names = ["Jack", "John", "Jane"]
base_salary = [700, 900, 1000]
bonus = ["10%", "20%", "5%"]
print(calculate_salary(zip(names, base_salary, bonus)))