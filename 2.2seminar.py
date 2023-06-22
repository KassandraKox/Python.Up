'''Создать список значений разных типов
для каждого вывести:'''
import sys

data = ['strike', 47, 47, 47.63, True, 1.0 + 5j]
for i, item in enumerate(data, start=1):
    print(f'№ = {i}; Value = {item}, id = {id(item)}; size = {sys.getsizeof(item)}; hash = {hash(item)}')
    if isinstance(item, int):
        print('int is True')
    if isinstance(item, str):
        print('str is True')
