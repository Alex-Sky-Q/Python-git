# 3

import random
import math

list1 = [random.randint(-100, 100) for i in range(15)]
print(list1)


def get_sqrt(seq):
    a = seq.copy()
    a = [round(math.sqrt(num), 1) if num >= 0 else num for num in a]
    return a


list2 = get_sqrt(list1)
print(list1)
print(list2)
