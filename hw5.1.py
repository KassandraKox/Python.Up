# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

# *path, file_name, file_extension = "C:\\Users\\proDream\\PycharmProjects\\GB_Python_2\\Seminar 5\\Seminar 5 HW\\task_1.py".replace('.', '\\').split('\\')
# path = '\\'.join(path)
# print(f"path = {path}\nfile_name = {file_name}\nfile_extension = {file_extension}")

def to_divide_path(path):
    *path, file_name, file_extension = path.replace('.', '\\').split('\\')
    path = '\\'.join(path)
    return path, file_name, file_extension


raw_path = "C:\\Users\\kapib\\PycharmProjects\\Python.Up\\hw5.1.py"
print("path = {}\nfile_name = {}\nfile_extension = {}".format(*to_divide_path(raw_path)))