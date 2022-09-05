# 3
good_result = 'Good condition'
norm_result = 'You have to check your calories consumption'
bad_result = 'You have to consult a physician'

name = input('Enter your name')
surname = input('Enter your surname')

while True:
    age = int(input('Enter your age'))
    if age >= 0:
        break

while True:
    weight = float(input('Enter your weight'))
    if weight >= 0:
        break

if weight < 50:
    if age < 40:
        result = norm_result
    else:
        result = bad_result
elif 50 <= weight < 120:
    result = good_result
elif weight >= 120:
    if age < 40:
        result = norm_result
    else:
        result = bad_result

print(name + ' ' + surname + ', ' + str(age) + ' years, ' + str(weight) + ' kg - ' + result)
print('{} {}, {} years, {} kg - {}'.format(name, surname, age, weight, result))
