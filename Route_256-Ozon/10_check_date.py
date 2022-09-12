# Задана дата в формате "день месяц год" в виде трёх целых чисел. Гарантируется, что:
# день — от 1 до 31,
# месяц — от 1 до 12,
# год — от 1950 до 2300.
# Проверьте, что заданные три числа соответствуют корректной дате (в современном григорианском календаре).
# В соответствии с современным календарём год високосный, если для этого года верно хотя бы одно из утверждений:
# делится на 4, но при этом не делится на 100;
# делится на 400.
# Например, годы 2012 и 2000 являются високосными, но годы 1999, 2022 и 2100 — нет.
# - Входные данные
# В первой строке записано целое число t (1≤t≤1000) — количество наборов входных данных в тесте. Наборы входных данных
# являются независимыми. Друг на друга они не влияют. Каждый набор входных данных задаётся одной строкой, в которой
# записаны три целых числа d, m, y (1≤d≤31,1≤m≤12,1950≤y≤2300) — день, месяц и год даты для проверки.
# 1
# 10 9 2022
# - Выходные данные
# Для каждого набора входных данных выведите YES, если соответствующая дата является корректной (т.е. существует
# такая дата в современном календаре). Выведите NO в противном случае.

from datetime import datetime

count = int(input())

for x in range(count):
    # date_list = map(int, input().split())
    # if date_list[2] % 400 == 0 or (date_list[2] % 4 == 0 and date_list[2] % 100 != 0):
    date_str = input()
    try:
        date_new = datetime.strptime(date_str, '%d %m %Y')
        print('YES')
    except ValueError:
        print('NO')
