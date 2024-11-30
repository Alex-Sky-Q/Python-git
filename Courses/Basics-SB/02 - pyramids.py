# Пирамида
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


# Яма
size = 5

for row in range(size):
    for col in range(size * 2):
        if row < col < size * 2 - row - 1:
            print('.', end='')
        elif col < size:
            print(size - col, end='')
        else:
            print(col + 1 - size, end='')
    print()
