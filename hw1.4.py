'''5. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна
 подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:

from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)'''

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
TRY_LIMIT = 10
try_num = 0

num = randint(LOWER_LIMIT, UPPER_LIMIT)

while TRY_LIMIT > 0:
    TRY_LIMIT -= 1
    try_num = int(input('Угадай загаданное число от 0 до 1 000: '))
    if try_num == num:
        print("Congratulations! You are lucky")
    elif (try_num < num):
        print(f'Твое число меньше. Осталось попыток {TRY_LIMIT}')
    else:
        print(f'Твое число больше. Осталось попыток {TRY_LIMIT}')
print(f'Загаданное число - {num}')




