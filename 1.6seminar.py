'''Напечатать таблицу умножения от 2*2 до 9*10 как на школьной тетради'''

START = 2
END = 11
HALF = 2

for i in range(START, END):
    for j in range(START, END // HALF + 1):
        print(f"{j:>2} X {i:>1} = {i * j:>2}", end="   ")
    print()
print()
for i in range(START, END):
    for j in range(END // HALF + 1, END - 1):
        print(f"{j:>2} X {i:>1} = {i * j:>2}", end="   ")
    print()
