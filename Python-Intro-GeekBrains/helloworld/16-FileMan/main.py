# main.py
import sys
import core as c

actions = {'list': 'View content of the folder',
           'create-folder': 'Create folder',
           'create-file': 'Create file',
           'copy': 'Copy object',
           'del': 'Delete object',
           'change-dir': 'Change folder',
           'game': 'Play the game'}

try:
    action = sys.argv[1]
except IndexError:
    print('Enter command')
    c.save_log(f'{IndexError} {sys.argv}')
else:
    if action == 'list':
        c.get_list()
    elif action == 'create-folder':
        try:
            c.create_folder(sys.argv[2])
        except IndexError:
            print('Please, specify folder name')
    elif action == 'create-file':
        try:
            if len(sys.argv) == 4:
                c.create_file(sys.argv[2], sys.argv[3])
            else:
                c.create_file(sys.argv[2])
        except IndexError:
            print('Please, specify file name')
    elif action == 'copy':
        try:
            if len(sys.argv) == 4:
                c.copy_obj(sys.argv[2], sys.argv[3])
            else:
                c.copy_obj(sys.argv[2])
        except IndexError:
            print('Please, specify object name')
    elif action == 'del':
        try:
            c.del_obj(sys.argv[2])
        except IndexError:
            print('Please, specify object name')
    elif action == 'change-dir':
        try:
            c.ch_dir(sys.argv[2])
        except IndexError:
            print('Please, specify folder name')
    elif action == 'game':
        sys.path.append('../')
        import GameNumber_6
    elif action == 'help':
        for key, value in actions.items():
            print(f'"{key}" - {value}')

    c.save_log(f'{action} {sys.argv}')
