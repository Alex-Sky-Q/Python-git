# Строка, состоящая из четырёх букв латинского алфавита ('a', 'b', 'c' и 'd'), закодирована след. образом:
# 'a' закодирована как 00;
# 'b' закодирована как 100;
# 'c' закодирована как 101;
# 'd' закодирована как 11.
# Например, в результате кодирования строки «badcac» получается «100001110100101».
# Для заданной последовательности цифр 0 и 1 осуществите декодирование в исходную строку.
# - Входные данные
# В первой строке входных данных записано целое число t (1≤t≤1000) — количество наборов входных данных. Наборы входных
# данных в тесте являются независимыми. Друг на друга они не влияют.
# Каждый набор входных данных задаётся одной строкой, состоящей из символов 0 и 1. Длина строки — от 2 до 50 символов.
# 1
# 100001110100101
# - Выходные данные
# Каждая строка должна содержать буквы 'a', 'b', 'c' и 'd' и являться ответом для соотв. набора входных данных

count = int(input())

for x in range(count):
    coded_nums = input()
    res = ''
    i = 0
    while i < (len(coded_nums) - 1):
        if coded_nums[i] == '0':
            res += 'a'
            i += 2
            continue
        else:
            if coded_nums[i+1] == '1':
                res += 'd'
                i += 2
                continue
            elif coded_nums[i+2] == '0':
                res += 'b'
                i += 3
                continue
            else:
                res += 'c'
                i += 3
    print(res)
