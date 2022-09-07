# Директор оценивает сотрудников по различным показателям и критериям.
# Один из этих критериев такой: приступив к заданию, сотрудник должен завершить его, не переключаясь на др. задания.
# Директор попросил от каждого сотрудника отчет о том, какие задания он выполнял в последние n дней. Отчет — это
# последовательность из n целых чисел a1,a2,…,an, где ai — идентификатор задания, которое сотрудник выполнял в i-й день.
# Необходимо написать программу, проверяющую, соответствует ли сотрудник критерию по его отчету.
# Сотрудник соответствует этому критерию, если не существует такого задания x, которое выполнялось с перерывом
# (т. е. в некоторый день i сотрудник выполнял задание x, в дни с i+1 по j−1 он занимался другими заданиями,
# а в день j сотрудник продолжил выполнение задания x, при этом j > i plus 1). Т.е. каждое задание, которое выполнял
# сотрудник, должно занимать один непрерывный отрезок дней.
# - Входные данные
# В первой строке задано одно целое число t (1≤t≤10) — количество наборов входных данных.
# Каждый набор входных данных состоит из двух строк. В первой строке задано одно целое число n (3≤n≤50000).
# Во второй строке заданы n целых чисел a1,a2,…,an (1≤ai≤n) — отчет сотрудника.
# - Выходные данные
# Для каждого набора входных данных выведите ответ на отд. строке.
# Если отчет соответствует критерию, выведите YES, иначе выведите NO.

# import time
# from collections import Counter

count = int(input())

for x in range(count):
    total_tasks = int(input())
    tasks = input().split()
    # start = time.perf_counter()
    # tasks = [int(num) for num in tasks_str]
    # tasks_cnt = {}
    # for i in tasks:
    #     if tasks_cnt.get(i):
    #         if tasks_cnt[i] == 2:
    #             continue
    #         else:
    #             tasks_cnt[i] += 1
    #     else:
    #         tasks_cnt[i] = 1
    # tasks_cnt = Counter(tasks)
    # tasks_to_check_list = [key for key, val in tasks_cnt.items() if val > 1]
    # Because iterator above works just once we need to store the list separately
    # tasks_to_check = set(tasks_to_check_list)
    # tasks_set = set(tasks)
    # if len(tasks_set) == len(tasks):
    #     print('YES')
    #     continue
    # We can create a dict with lists of indexes of each item
    tasks_dict = {}
    for i, task in enumerate(tasks):
        if tasks_dict.get(task):
            tasks_dict[task].append(i)
        else:
            tasks_dict[task] = [i]
    res = ''
    # Compare indexes of each task with each other
    for ind in tasks_dict.values():
        if len(ind) >= 2:
            for i, v in enumerate(ind[:-1]):
                diff = ind[i+1] - v
                if diff > 1:
                    res = 'NO'
                    print(res)
                    break
        if res:
            break
    if not res:
        print('YES')

    # for i, task in enumerate(tasks[:-2]):
    #     if task == tasks[i+1]:
    #         continue
    #     if task in tasks_to_check:
    #         # if bin_search(task, tasks[i+2:]):
    #         for ind in tasks_dict[task]:
    #             if ind >= (i+2):
    #                 res = 'NO'
    #                 print(res)
    #                 break
    #     if res:
    #         break
    # if not res:
    #     print('YES')

    # print((time.perf_counter() - start))


# def bin_search(s, data):
#     data_sorted = sorted(set(data))
#     if len(data_sorted) == 1:
#         if s == data_sorted[0]:
#             return True
#         else:
#             return False
#     b = int(len(data_sorted) / 2)
#     while len(data_sorted) != 1:
#         if s == data_sorted[b]:
#             return True
#         if s < data_sorted[b]:
#             data_sorted = data_sorted[:b]
#             b = int(len(data_sorted) / 2)
#             if len(data_sorted) == 1:
#                 if s == data_sorted[0]:
#                     return True
#                 else:
#                     return False
#         else:
#             if (b + 1) < len(data_sorted):
#                 data_sorted = data_sorted[b+1:]
#             else:
#                 return False
#             b = int(len(data_sorted) / 2)
#             if len(data_sorted) == 1:
#                 if s == data_sorted[0]:
#                     return True
#                 else:
#                     return False
#     return False
