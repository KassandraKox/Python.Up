'''ввести число от1 до 999, используя мат.операции с числами
сообщить что введено, число, двузначное или трехзначное
если 1 - вывести квадрат
2 - произведение цифр
3 - зеркальное отображение
без магических чисел'''

MIN_D = 0
MAX_D = 1000
ONE_DIGIT = 10
TWO_DIGIT = 100
result = 0
number_type = ''
'''def check_input():
    while True:
        num = input('Введите число: ')
        if num.isdecimal() and MIN_D < (res:=int(num)) < MAX_D:
            return num
        print('Введено неверное значение.')

num = check_input()'''
# ошибка int str
while True:
    n = int(input("Введите число от 1 до 999: "))
    if MIN_D < n < MAX_D:
        if n // ONE_DIGIT == 0:
            number_type = "Цифра"
            result = n ** 2
        elif n // TWO_DIGIT == 0:
            number_type = "Двузначное число"
            result = (n // ONE_DIGIT) * (n % ONE_DIGIT)
        else:
            number_type = "Трёхзначное число"
            result = n % ONE_DIGIT * TWO_DIGIT + n // ONE_DIGIT % ONE_DIGIT * ONE_DIGIT + n // TWO_DIGIT
        break

print(number_type, '=', result)
