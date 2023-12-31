# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>
from pathlib import Path


def mass_rename(path, old_ext, new_ext, new_name):
    directory = Path(path)
    file_to_rename = [i for i in directory.iterdir() if i.suffix[1:] == old_ext]
    for enum, file in enumerate(file_to_rename, start=1):
        Path.rename(file, Path(f"{path}/{file.stem}_{new_name}_{enum}.{new_ext}") )

if __name__ == '__main__':
    mass_rename('../out/hw_7', 'txt', 'text', 'text_file')