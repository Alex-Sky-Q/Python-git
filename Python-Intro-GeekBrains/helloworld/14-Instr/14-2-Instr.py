import random

list1 = [random.randint(-100, 100) for i in range(15)]
print(list1)

list2 = [num for num in list1 if num > 0 and num % 3 == 0 and num % 4 != 0]
print(list2)
