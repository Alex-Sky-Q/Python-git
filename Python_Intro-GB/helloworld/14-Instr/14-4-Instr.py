# 4


def get_pow13(val):
    try:
        if val != 13:
            a = val ** 2
        else:
            raise ValueError('You found it')
        return a
    except ValueError:
        print('Try to use another way')
        return 'Error'


while True:
    user_num = ''
    while user_num not in range(1, 101):
        user_num = int(input('Enter the number (1-100): '))

    result = get_pow13(user_num)

    if result != 'Error':
        print(result)
        break
