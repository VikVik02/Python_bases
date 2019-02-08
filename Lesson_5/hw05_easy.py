# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os

def make_directory():
    for i in range(1, 10)
        dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print("Директория с данным именем уже есть в папке")

def delete_directory():
    for i in range(1, 10)
        dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        try:
            os.rmdir(dir_path)
        except FileNotFoundError:
            print("Директории с данным именем нет в папке")

make_directory()
delete_directory()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
#ТОЛЬКО ПАПКИ, А НЕ ФАЙЛЫ!

dir_list = os.listdir()
only_dir = []
for d in dir_list:
    if os.path.isdir(d):
        only_dir.append(d)
print(only_dir)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# ИСПОЛЬЗОВАТЬ ТОЛЬКО МОДУЛЬ OS
import shutil

def duplicate_file():
    base_name = os.path.basename(__file__)
    file_path = os.path.join(os.getcwd(), 'copy_{}'.format(base_name))
    shutil.copyfile(__file__, file_path)

duplicate_file()