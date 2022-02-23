# core.py
import os
import shutil
import datetime


def get_list(folders_only=False):
    if folders_only:
        res = [f for f in os.listdir() if os.path.isdir(f)]
    else:
        res = os.listdir()
    print(res)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print(f'Folder "{name}" already exists')
    else:
        print(f'Folder "{name}" created')


def create_file(name, text=None):
    try:
        with open(name, 'w', encoding='utf-8') as f:
            if text:
                f.write(text)
    except PermissionError:
        print(f'Permission denied. Maybe folder "{name}" already exists')
    else:
        print(f'File "{name}" created')


def copy_obj(name, new_name=None):
    if not new_name:
        new_name = f'Copy of {name}'
    try:
        if os.path.isdir(name):
            try:
                shutil.copytree(name, new_name)
                print(f'Folder "{name}" copied to "{new_name}"')
            except FileExistsError:
                print(f'Folder "{new_name}" already exists')
        else:
            shutil.copy(name, new_name)
            print(f'File "{name}" copied to "{new_name}"')
    except FileNotFoundError:
        print(f'Object "{name}" not found')


def del_obj(name):
    try:
        if os.path.isdir(name):
            os.rmdir(name)
            print(f'Folder "{name}" deleted')
        else:
            os.remove(name)
            print(f'File "{name}" deleted')
    except FileNotFoundError:
        print(f'Object "{name}" not found')


def ch_dir(name):
    try:
        os.chdir(name)
    except FileNotFoundError:
        print(f'Folder "{name}" not found')


def save_log(message=None):
    text = f'{datetime.datetime.now()} - {message} \n'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(text)


if __name__ == '__main__':
    save_log('123')
    # create_file('test.txt')
    # copy_obj('test.txt')
    # del_obj()
