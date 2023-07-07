# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.
# Для простоты будем использовать только положительную индексацию

def range_sum(nums, start, end):
    if start > end:
        start, end = end, start
    if end + 1 >= len(nums):
        end = len(nums)
    return sum(nums[i] for i in range(start, end))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start = int(input('Введите стартовое значение:'))
end = int(input('Введите конечное значение:'))
print(range_sum(numbers, start, end))