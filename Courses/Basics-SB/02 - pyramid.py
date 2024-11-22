size = 5
next_num = 1

for row in range(size):
    last_is_num = False
    for col in range(size * 2 - 1):
        if size - 1 - row <= col <= size - 1 + row and not last_is_num:
            print(next_num, end='')
            last_is_num = True
            next_num += 2
        else:
            print(end='  ')
            last_is_num = False
    print()
