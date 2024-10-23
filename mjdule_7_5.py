import os
from os import walk


# folder path
dir_path = r'D:\\Доки\Програмирование\Python\lessons\upgrade\pythonProject\\'
# list to store files
res = []
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
print(res)

# folder path
dir_path = r'D:\\Доки\Програмирование\Python\lessons\upgrade\pythonProject\\'
# list file and directories
res = os.listdir(dir_path)
print(res)

# folder path
dir_path = r'D:\\Доки\Програмирование\Python\lessons\upgrade\pythonProject\\'
# list to store files name
res = []
for (dir_path, dir_names, file_names) in walk(dir_path):
    res.extend(file_names)
print(res)

# folder path
dir_path = r'D:\\Доки\Програмирование\Python\lessons\upgrade\pythonProject\\'
res = []
for (dir_path, dir_names, file_names) in walk(dir_path):
    res.extend(file_names)
    # don't look inside any subdirectory
    break
print(res)

# https://pythonturbo.ru/kak-vyvesti-spisok-fajlov-v-kataloge-na-python/?ysclid=m2l5jl17r358205774
# Задание:
#
# Создайте новый проект или продолжите работу в текущем проекте.
#
#     Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
#     Примените os.path.join для формирования полного пути к файлам.
#     Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
#     Используйте os.path.getsize для получения размера файла.
#     Используйте os.path.dirname для получения родительской директории файла.
#
#
# Комментарии к заданию:
#
# Ключевая идея – использование вложенного for
#
#     for root, dirs, files in os.walk(directory):
#
#       for file in files:
#
#         filepath = ?
#
#         filetime = ?
#
#         formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#
#         filesize = ?
#
#         parent_dir = ?
#
#         print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
#
#
#
#
# Так как в разных операционных системах разная схема расположения папок, тестировать проще всего в папке проекта (directory = “.”)
# Пример возможного вывода:
# Обнаружен файл: main.py, Путь: ./main.py, Размер: 111 байт, Время изменения: 11.11.1111 11:11, Родительская директория.

# Функция os.path.join() в Python используется для объединения нескольких путей. Она учитывает особенности
# операционной системы и добавляет соответствующий разделитель между пут
# import os
#
# path1 = "folder1"
# path2 = "folder2"
# path3 = "file.txt"
# result = os.path.join(path1, path2, path3)
# print(result)  # Вывод: folder1/folder2/file.txt [1](https://sky.pro/media/kak-rabotat-s-modulem-os-path-v-python/)

