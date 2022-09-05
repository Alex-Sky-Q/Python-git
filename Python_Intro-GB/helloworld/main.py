# 1
number = int(input('Enter the number'))
number += 2
print(number)

# 2
while True:
    number = int(input('Enter the number'))
    if 0 < number < 10:
        number **= 2
        break
    else:
        print('The number should be between 0 and 10')

print(number)