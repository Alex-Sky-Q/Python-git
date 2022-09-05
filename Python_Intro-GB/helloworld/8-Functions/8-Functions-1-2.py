# 1


def get_info(name, age, city):
    result = f'{name}, {age} years, lives in {city} city'
    return result


user_name = input('Enter name: ')

while True:
    user_age = int(input('Enter age: '))
    if user_age >= 0:
        break

user_city = input('Enter city: ')

print(get_info(user_name, user_age, user_city))

# 2


def find_max(a, b, c):
    result = max(a, b, c)
    return result


num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))
num3 = int(input('Enter number 3: '))

print(find_max(num1, num2, num3))
