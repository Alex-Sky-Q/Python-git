# Task. Write a simple calculator program – a console application
# (implement at least 4 operations: addition, subtraction, multiplication, division)
# with input / output of values / results

# Solution. Can be improved for complex expressions with several operators

user_expr = input('Please, enter the expression\n')

expression = []
temp_value = ''

for s in user_expr:
    if not s.isspace():
        if not s.isnumeric():
            expression.append(float(temp_value))
            expression.append(s)
            temp_value = ''
            continue
        temp_value += s

expression.append(float(temp_value))
print(expression)

if '+' in expression:
    res = expression[0] + expression[2]
elif '-' in expression:
    res = expression[0] - expression[2]
elif '*' in expression:
    res = expression[0] * expression[2]
elif '/' in expression:
    res = expression[0] / expression[2]
else:
    res = 'Unknown operator'

print(res)
