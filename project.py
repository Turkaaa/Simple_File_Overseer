import time
import os
from datetime import datetime

def list_files():
    files_info = []
    for file_name in os.listdir('.'):
        if os.path.isfile(file_name):
            size = os.path.getsize(file_name)
            files_info.append((file_name, size))
    return files_info

def display_files_info(files_info):
    for filename, size in files_info:
        if language == 1:
            print(f'File - {filename}, size - {size / 1024} KB')
            if size > 100 * 1024:
                print(f'Warning - file {filename} > 100 KB!!!')
        elif language == 0:
            print(f'Файл - {filename}, размер - {size / 1024} KB')
            if size > 100 * 1024:
                print(f'Внимание - {filename} больше 100 KB!!!')


def get_file_info(files_info):
    while True:
        if language == 0:
            user_input = input('Введите название файла для проверки (или exit для выхода): ')
            if user_input == 'exit':
                break
            found = False
            for filename, size in files_info:
                if filename == user_input:
                    found = True
                    timestamp = os.path.getmtime(filename)1
                    dt_object = datetime.fromtimestamp(timestamp)
                    formatted_time = dt_object.strftime('%Y-%m-%d %H:%M:%S')
                    print(f'Файл - {filename} найден, время последнего использования - {formatted_time}')
                    break
            if not found:
                print('Внимание: файл не найден!!!')

        elif language == 1:
            user_input = input('Enter the file name to check (or exit to exit): ')
            if user_input == 'exit':
                break
            found = False
            for filename, size in files_info:
                if filename == user_input:
                    found = True
                    timestamp = os.path.getmtime(filename)
                    dt_object = datetime.fromtimestamp(timestamp)
                    formatted_time = dt_object.strftime('%Y-%m-%d %H:%M:%S')
                    print(f'File - {filename} exist, last modified time - {formatted_time}')
                    break
            if not found:
                print('Warning: file not found!!!')


files_info = list_files()
language = int(input('En, ru? (1 or 0)'))
if language == 0:
    print('Вас приветствует файловый смотритель!!!')
    while True:
        print('!!!Меню!!!\n 1.Просмотр файлов\n 2.Поиск файла\n 3.Выход')
        user = int(input('Выберите цифрой пункт меню: '))
        if user == 1:
            display_files_info(files_info)
        elif user == 2:
            get_file_info(files_info)
        elif user == 3:
            exit()
elif language == 1:
    print('Welcome to the File Overseer!!!')
    while True:
        print('!!!Menu!!!\n 1.View files\n 2.Search for a file\n 3.Exit')
        user = int(input('Select a menu item with a number: '))
        if user == 1:
            display_files_info(files_info)
        elif user == 2:
            get_file_info(files_info)
        elif user == 3:
            exit()