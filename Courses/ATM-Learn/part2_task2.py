# Compare speed of work (adding element, search of element, deleting of element) for the following collections:
# •	Lists (ArrayList vs LinkedList) -> list in python
# •	Sets (HashSet vs TreeSet) -> set in python
# •	Maps (HashMap vs TreeMap) -> dict in python
# Note: To get more representative results it is recommended to use 10000+ elements in the collections
from timeit import timeit

test_list = [x for x in range(11000)]
test_set = {x for x in range(11000)}
test_dict = {x: y for x, y in enumerate(range(-11000, 0))}
# test_dict = {x:y for x,y in zip(test_list, test_tuple)}
# print(test_dict.get(100))

print('Adding elements')
res = timeit(lambda: test_list.append('A'), number=30000)
print(f'Adding elements to a list. Time (x1000): {res * 1000}')

res = timeit(lambda: test_set.add('A'), number=30000)
print(f'Adding elements to a set. Time (x1000): {res * 1000}')

res = timeit(lambda: test_dict.update({15: 'A'}), number=30000)
print(f'Adding elements to a dict. Time (x1000): {res * 1000}')


print('Deleting elements')
res = timeit(lambda: test_list.remove('A'), number=1)
print(f'Del elements from a list. Time (x1000): {res * 1000}')

res = timeit(lambda: test_set.remove('A'), number=1)
print(f'Del elements from a set. Time (x1000): {res * 1000}')

res = timeit(lambda: test_dict.pop(15), number=1)
print(f'Del elements from a dict. Time (x1000): {res * 1000}')


print('Searching elements')
res = timeit(lambda: 6000 in test_list, number=10000)
print(f'Search elements in a list. Time (x1000): {res * 1000}')

res = timeit(lambda: 6000 in test_set, number=10000)
print(f'Search elements in a set. Time (x1000): {res * 1000}')

res = timeit(lambda: -6000 in test_dict, number=10000)
print(f'Search keys in a dict. Time (x1000): {res * 1000}')

res = timeit(lambda: -6000 in test_dict.values(), number=10000)
print(f'Search values in a dict. Time (x1000): {res * 1000}')
