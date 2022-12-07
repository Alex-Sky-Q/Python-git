# Задан набор комментариев. Каждый комментарий описывается тремя параметрами:
# - своим идентификатором (уникальное целое число от 1 до 109)
# - идентификатором предка (или -1, если предка нет)
# - своим текстом (непустая строка длиной не более 100 из символов с кодами от 32 до 126, включительно).
# Выведите заданные комментарии в древесном виде, отформатировав их в точности как изображено в примерах. Для каждого
# комментария-родителя его детей надо выводить в порядке увеличения их идентификаторов. Т.е. всех детей одного родителя
# надо упорядочивать по возрастанию их идентификаторов.
# Можно выводить произвольное кол-во пробелов в конце строки. Например, при выводе «| | |» допустимо вывести «| | | »
# - Входные данные
# Наборы входных данных в тесте являются независимыми. Друг на друга они не влияют.
# В первой строке записано целое число t (1≤t≤100) — количество наборов входных данных в тесте.
# Далее следуют t наборов входных данных.
# Каждый набор входных данных начинается строкой, которая содержит целое число n (1≤n≤200) — количество комментариев.
# Далее заданы сами комментарии, по одному в строке. Каждая строка имеет вид «id p text», где id — идентификатор
# комментария, p — идентификатор предка, text — текст комментария.
# Гарантируется, что комментарии корректны — задают одно или более дерево комментариев (циклических зависимостей нет,
# если указан родитель, то он существует).
# 1
# 6
# 10 -1 x
# 20 10 x
# 40 -1 x
# 50 -1 x
# 11 20 x
# 30 10 x
# - Выходные данные
# Выведите комментарии в виде деревьев. Между выводами для разных наборов входных данных выводите пустую строку.
# x
# |
# |--x
# |  |
# |  |--x
# |
# |--x
#
# x
#
# x


def print_comments(start_comm, from_dict, level=0, parent=0, cnt=0, from_one=False):
    if level == 0 and parent == 0:
        print(comm_text_dict[start_comm])
    elif level > 0:
        if parent > 0 and cnt > 0 and from_one:
            print((level) * '|  ' + (parent-1) * '   ' + '|--' + str(comm_text_dict[start_comm]))
        elif parent > 0 and cnt == 0 and from_one:
            print((level-1) * '|  ' + (parent) * '   ' + '|--' + str(comm_text_dict[start_comm]))
        else:
            print((level-1) * '|  ' + (parent) * '   ' + '|--' + str(comm_text_dict[start_comm]))
    else:
        if parent > 0 and cnt > 0 and from_one:
            print((level) * '|  ' + (parent -1) * '   ' + '|--' + str(comm_text_dict[start_comm]))
        elif parent > 0 and cnt == 0 and from_one:
            print((level-1) * '|  ' + (parent -1) * '   ' + '|--' + str(comm_text_dict[start_comm]))
        else:
            print((level-1) * '|  ' + (parent) * '   ' + '|--' + str(comm_text_dict[start_comm]))
    if from_dict[start_comm]:
        if len(from_dict[start_comm]) > 1:
            cnt = len(from_dict[start_comm])
            for s in sorted(from_dict[start_comm]):
                level += 1
                cnt -= 1
                if level == 0 and parent == 0:
                    print('|  ')
                elif level > 1:
                    if parent > 0 and cnt > 0:
                        print((level-1) * '|  ' + (parent) * '   ' + '|')
                    elif parent > 0 and cnt == 0:
                        print((level - 1) * '|  ' + (parent) * '   ' + '|')
                    else:
                        print((level - 1) * '|  ' + (parent) * '   ' + '|')
                else:
                    if parent > 0:
                        print((level - 1) * '|  ' + (parent) * '   ' + '|')
                    else:
                        print((level - 1) * '|  ' + (parent) * '   ' + '|')
                print_comments(s, from_dict, level, parent, cnt)
                level -= 1
        else:
            parent += 1
            if level == 0 and parent == 1:
                print('|  ')
            elif level == 0:
                if parent > 0 and cnt > 0:
                    print((level) * '|  ' + (parent-1) * '   ' + '|')
                elif parent > 0 and cnt == 0:
                    print((level - 1) * '|  ' + (parent-1) * '   ' + '|')
                else:
                    print((level - 1) * '|  ' + (parent) * '   ' + '|')
            else:
                if parent > 0 and cnt > 0:
                    print((level) * '|  ' + (parent -1) * '   ' + '|')
                elif parent > 0 and cnt == 0:
                    print((level-1) * '|  ' + (parent ) * '   ' + '|')
                else:
                    print((level - 1) * '|  ' + (parent) * '   ' + '|')
            print_comments(from_dict[start_comm][0], from_dict, level, parent, cnt, True)
            #parent -= 1
        # if level != 0:
        #     print('|')


count = int(input())

for x in range(count):
    comm_total = int(input())
    base_comments = []
    comm_dict = {}
    comm_text_dict = {}
    for c in range(comm_total):
        comm_id, par_id, comm_text = input().split(maxsplit=2, sep=' ')
        comm_text_dict[int(comm_id)] = comm_text
        if int(par_id) == -1:
            base_comments.append(int(comm_id))
        if not comm_dict.get(int(comm_id)):
            comm_dict[int(comm_id)] = []
        if comm_dict.get(int(par_id)):
            comm_dict[int(par_id)].append(int(comm_id))
        else:
            comm_dict[int(par_id)] = [int(comm_id)]

    base_comments.sort()

    # print(base_comments)
    # print(comm_dict)

    for b in base_comments:
        print_comments(b, comm_dict)
        print()


# def print_comments(start_comm, from_dict, levels=None, start=0):
#     if levels is None:
#         levels = [0]
#
#     if start == 1:
#         print(comm_text_dict[start_comm])
#     else:
#         comment_line = ['' * levels[-1]]
#         for lvl in levels:
#             comment_line.insert(lvl, '|  ')
#         print(''.join(comment_line) + '|--' + comm_text_dict[start_comm])
#
#     if from_dict[start_comm]:
#         connection_line = ['' * levels[-1]]
#         for lvl in levels:
#             connection_line.insert(lvl, '|  ')
#         print(''.join(connection_line))
#         for s in sorted(from_dict[start_comm]):
#             print_comments(s, from_dict, levels)
#             lvl = levels[-1]
#             levels.remove(lvl)
#             lvl += 1
#             levels.append(lvl)
