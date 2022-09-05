from MakeDir import make_dir, remove_dir
import RandomValue as rv

test_list = [1, 2, 3, 4]

print(rv.rand_val(test_list))

dir_num = int(input('How many folders create? '))

for i in range(dir_num):
    dir_name = f'dir_{i+1}'
    make_dir(dir_name)

dir_del = input('Which folder to delete? ')

if dir_del:
    remove_dir(dir_del)
else:
    print('The End')
