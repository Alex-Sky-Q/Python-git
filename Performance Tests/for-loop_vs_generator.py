import random
import timeit
import tracemalloc


def sum_arr(arr):
    return sum(x for x in arr if x > 0)


def sum_arr_for(arr):
    s = 0
    for n in arr:
        if n > 0:
            s += n
    return s


arr = random.sample(range(-100000, 100000), 100000)

# tracemalloc.start()

# sum_arr(arr)
# sum_arr_for(arr)

# snapshot = tracemalloc.take_snapshot()
# top_stats = snapshot.statistics('lineno')

# print("[ Top 10 ]")
# for stat in top_stats[:10]:
#     print(stat)

res_gen = timeit.timeit(lambda: sum_arr(arr), number=1000)
res = timeit.timeit(lambda: sum_arr_for(arr), number=1000)

print(f'res generator is {res_gen}')
print(f'res for loop is {res}')

# Python 3.11.1
# res generator is 7.87187160004396
# res for loop is 5.097717300057411

# Python 3.10.4:
# res generator is 6.315166200045496
# res for loop is 5.650368899921887

# Python 3.8:
# res generator is 6.869236399999999
# res for loop is 6.514139899999999

# 3.7.4 and 3.9.9 - generator is faster
# 3.6.3, 3.6.5, 3.8, 3.10.4 and 3.11.1 - for loop is faster

# for loop is constantly faster than sum().
# Also tests with tracemalloc show that for loop is more efficient in terms of memory.
# It seems logical since probably we do not create any intermediate object to pass to a sum().
# And we just need to apply a function to list's elements and do not need a new list.
