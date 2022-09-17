# Для n отелей были проведены опросы, по результатам которых каждый отель получил некоторое количество голосов.
# Задан массив неотрицательных целых чисел v1,v2,…,vn, где vi — количество голосов у отеля i.
# Теперь отелям надо назначить звёзды — от одной до пяти звёзд каждому отелю. Должны выполняться следующие требования:
# - каждый отель должен получить некоторое целое количество звёзд (от 1 до 5, включительно);
# - если у отеля a звёзд строго больше чем у отеля b, то количество голосов за отель a строго больше чем за отель b
# (однако отели с одинаковым количеством звёзд могут иметь разное число голосов);
# - для каждого количества звёзд от 1 до 5 есть хотя бы один отель с таким количеством звёзд;
# - 1-звёздных отелей должно быть строго больше чем 2-звёздных, 2-звёздных должно быть строго больше чем 3-звёздных,
# 3-звёздных строго больше чем 4-звёздных и, наконец, 4-звёздных строго больше чем 5-звёздных.
# По заданным количествам голосов v1,v2,…,vn назначьте звёзды так, чтобы все требования выше были выполнены. Если это
# можно сделать несколькими способами, найдите любой из них.
# Эта задача сначала стоила 25 баллов, но потом мы нашли для неё хитрые тесты и обнаружили, что естественное решение
# может давать неоптимальный ответ. Поэтому мы добавили эти тесты и назначили им стоимость 15 баллов. Эти тесты
# отсутствуют в предоставленном архиве тестов. Они секретные, кроме одного (тест 61). Считайте это особой задачей со
# звёздочкой — написать такое решение, которое проходит и их (это не так и просто). Решения, которые проходят
# упрощённый набор тестов оцениваются из 25 баллов.
# - Входные данные
# В первой строке записано целое число t (1≤t≤104) — количество наборов входных данных в тесте.
# Наборы входных данных являются независимыми. Друг на друга они не влияют.
# Первая строка каждого набора входных данных содержит целое число n (15≤n≤4⋅105) — количество отелей.
# Вторая строка набора содержит последовательность количеств голосов v1,v2,…,vn (0≤vi≤109), где vi — целое число,
# которое обозначает количество голосов за i-й отель.
# 1
# 15
# 10 20 30 40 50 60 70 80 90 100 110 120 130 140 150
# - Выходные данные
# Для каждого набора входных данных выведите в строку n целых чисел s1,s2,…,sn (1≤si≤5), где si — количество звёзд
# у i-го отеля. Если вариантов назначения звёзд несколько, то выведите любой из них. Если искомого способа назначить
# звёзды не существует, то выведите n чисел -1

from collections import Counter


def combos(from_list):
    return ((a, b, c) for a in from_list for b in from_list for c in from_list)


def create_stars(from_list, to_dict, bs5=None, bs4=None, bs3=None):
    i = 5
    for v in from_list:
        while i > 0:
            to_dict[i]['vote_min'] = v[0]
            to_dict[i]['cnt'] += v[1]
            if i == 5 or to_dict[i]['cnt'] > to_dict[i + 1]['cnt']:
                if i == 5:
                    if bs5 == 0:
                        i -= 1
                    else:
                        bs5 -= 1
                elif i == 4:
                    if bs4 == 0:
                        i -= 1
                    else:
                        bs4 -= 1
                elif i == 3:
                    if bs3 == 0:
                        i -= 1
                    else:
                        bs3 -= 1
                else:
                    i -= 1
            break
    if to_dict[1]['cnt'] <= to_dict[2]['cnt'] or to_dict[2]['cnt'] <= to_dict[3]['cnt'] \
            or to_dict[3]['cnt'] <= to_dict[4]['cnt'] or to_dict[4]['cnt'] <= to_dict[5]['cnt']:
        return False
    else:
        return True


count = int(input())

for x in range(count):
    hotels_count = int(input())
    hotels_list = []
    for hotel in input().split():
        hotels_list.append(int(hotel))
    # print(hotels_list)
    # [5, 12, 6, 0, 9, 0, 13, 6, 4, 17, 9, 5, 4, 13, 5, 13, 6, 5, 4, 5, 4, 17, 3, 5, 21, 3]

    dict_n = Counter(hotels_list)
    if len(dict_n) < 5:
        print('-1 ' * hotels_count)
        continue
    # print(dict_n)
    # {5: 6, 12: 1, 6: 3, 0: 2, 9: 2, 13: 3, 4: 4, 17: 2, 3: 2, 21: 1}
    votes_list = sorted(dict_n.items(), reverse=True)
    # print(votes_list)
    # [(21, 1), (17, 2), (13, 3), (12, 1), (9, 2), (6, 3), (5, 6), (4, 4), (3, 2), (0, 2)]

    res = False
    for s in combos(range(len(votes_list)-4)):
        bs5, bs4, bs3 = s
        dict_stars = {5: {'vote_min': 0, 'cnt': 0}, 4: {'vote_min': 0, 'cnt': 0},
                      3: {'vote_min': 0, 'cnt': 0}, 2: {'vote_min': 0, 'cnt': 0}, 1: {'vote_min': 0, 'cnt': 0}}
        res = create_stars(votes_list, dict_stars, bs5=bs5, bs4=bs4, bs3=bs3)
        if res:
            break

    if not res:
        print('-1 ' * hotels_count)
        continue

    # print(dict_stars)

    for h in hotels_list:
        if h >= dict_stars[5]['vote_min']:
            print(5, end=' ')
        elif h >= dict_stars[4]['vote_min']:
            print(4, end=' ')
        elif h >= dict_stars[3]['vote_min']:
            print(3, end=' ')
        elif h >= dict_stars[2]['vote_min']:
            print(2, end=' ')
        else:
            print(1, end=' ')

    print()


# Simple solution , doesn't work for all cases
# def create_stars(from_list, to_dict):
#     i = 5
#     for v in from_list:
#         while i > 0:
#             to_dict[i]['vote_min'] = v[0]
#             to_dict[i]['cnt'] += v[1]
#             if i == 5 or to_dict[i]['cnt'] > to_dict[i + 1]['cnt']:
#                 i -= 1
#             break
    # create_stars(votes_list, dict_stars)
    # if dict_stars[1]['cnt'] < dict_stars[2]['cnt'] or dict_stars[2]['cnt'] < dict_stars[3]['cnt']\
    #         or dict_stars[3]['cnt'] < dict_stars[4]['cnt'] or dict_stars[4]['cnt'] < dict_stars[5]['cnt']:
    #     print('-1 ' * hotels_count)
    #     continue


# Example when simple solution doesn't work
# [(93, 2), (62, 1), (50, 3), (44, 1), (34, 10), (31, 2), (23, 2), (22, 13), (20, 1), (11, 15)]
# 5 2 93
# 4 4 62, 50
# 3 11 44, 34
# 2 17 31, 23, 22
# 1 16 20, 11
# This is the way how it can be solved with an improved algorithm
# 5 2 93
# 4 5 62, 50, 44
# 3 12 34, 31
# 2 15 23, 22
# 1 16 20, 11

# An attempt to create a backtracking algorithm.
# It works only when the solution can be found by steps increase for just one of the stars count
# def create_stars(dictionary, bs=None, step=None, at=None, num=None):
#     i = 5 if not step else step
#     n = 0 if not num else num
#     back_step = 0 if not bs else bs
#     attempts = 0 if not at else at
#     while i > 0:
#         found = False
#         while not found:
#             if n < len(votes_list):
#                 dictionary[i]['cnt'] = 0
#                 for v in votes_list[n:]:
#                     dictionary[i]['vote_min'] = v[0]
#                     dictionary[i]['cnt'] += v[1]
#                     n += 1
#                     if i == 5 or dictionary[i]['cnt'] > dictionary[i+1]['cnt']:
#                         if back_step > 0:
#                             back_step -= 1
#                             continue
#                         else:
#                             found = True
#                             break
#             break
#         if i <= 3 and dictionary[i]['cnt'] < dictionary[i+1]['cnt']:
#             back_step = attempts + 1
#             attempts += 1
#             if i == 3:
#                 num = 0
#             else:
#                 num = votes_list.index((dictionary[i+3]['vote_min'], dict_n[dictionary[i+3]['vote_min']]))+1
#             if attempts < len(votes_list):
#                 create_stars(dictionary, bs=back_step, step=(i+2), at=attempts, num=num)
#             else:
#                 break
#         i -= 1
