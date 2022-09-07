# Задан набор отрезков времени. Каждый отрезок задан в формате HH:MM:SS-HH:MM:SS, т.е.
# сначала часы, минуты и секунды левой границы отрезка, а затем часы, минуты и секунды правой границы.
# Необходимо выполнить валидацию заданного набора отрезков времени. Т.е. проверить следующие условия:
# - часы, мин. и сек. заданы корректно (т.е. часы находятся в промежутке от 0 до 23, а мин. и сек. — от 0 до 59);
# - левая граница отрезка находится не позже его правой границы (но границы могут быть равны);
# - никакая пара отрезков не пересекается (даже в граничных моментах времени).
# Необходимо вывести YES, если заданный набор отрезков времени проходит валидацию, и NO в противном случае.
# Необходимо проверить t независимых наборов тестовых данных.
# - Входные данные
# Первая строка входных данных содержит одно целое число t (1≤t≤10) — кол-во наборов тестовых данных
# Первая строка набора содержит одно целое число n (1≤n≤2⋅104) — кол-во отрезков времени.
# В след. n строках - описания отрезков. Описание отрезка времени задано в формате HH:MM:SS-HH:MM:SS,
# где HH, MM и SS — последовательности из двух цифр. Пробелов в описании формата нет.
# Также ни в одном описании нет пробелов в начале и конце строки.
# - Выходные данные
# Для каждого набора тестовых данных выведите ответ — YES, если заданный набор отрезков времени проходит валидацию,
# и NO в противном случае. Ответы выводите в порядке следования наборов во входных данных.

from datetime import time


# Check that no time borders overlap
def time_pers_check(time_list):
    times = sorted(time_list)
    for i, t in enumerate(times[:-1]):
        diff = times[i+1][0] > t[1]
        if not diff:
            return False
    return True


count = int(input())

for x in range(count):
    total_time_pers = int(input())
    time_pers_str = []
    for y in range(total_time_pers):
        time_pers_str.append(input().split('-'))
    res = ''
    time_pers = []
    for t_str in time_pers_str:
        try:
            temp_list = (time.fromisoformat(t_str[0]), time.fromisoformat(t_str[1]))
        except ValueError:
            res = 'NO'
            print(res)
            break
        if temp_list[1] < temp_list[0]:
            res = 'NO'
            print(res)
            break
        time_pers.append(temp_list)
    if len(time_pers) >= 2:
        if not time_pers_check(time_pers):
            res = 'NO'
            print(res)
    if not res:
        print('YES')
