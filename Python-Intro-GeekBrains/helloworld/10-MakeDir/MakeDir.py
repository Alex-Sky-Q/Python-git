# 1

import os


def make_dir(dirname):
    # path = os.path.join(os.getcwd(), dirname)
    os.mkdir(dirname)
    print(f'{dirname} created')


def remove_dir(dirname):
    # path = os.path.join(os.getcwd(), dirname)
    os.rmdir(dirname)
    print(f'{dirname} deleted')
