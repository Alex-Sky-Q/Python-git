# Реализовать валидацию корректности карты для стратегической компьютерной игры.
# Карта состоит из гексагонов (шестиугольников), каждый из которых принадлежит какому-то региону карты. В файлах игры
# карта представлена как n строк по m символов в каждой (строки и символы в них нумеруются с единицы). Каждый нечетный
# символ каждой четной строки и каждый четный символ каждой нечетной строки — точка (символ . с ASCII кодом 46);
# все остальные символы соответствуют гексагонам и являются заглавными латинскими буквами. Буква указывает
# на то, какому региону принадлежит гексагон.
# Необходимо проверить, что каждый регион карты является одной связной областью. Т.е. не должно быть двух гексагонов,
# принадлежащих одному и тому же региону, которые не соединены др. гексагонами этого же региона.
# - Входные данные
# В первой строке задано одно целое число t (1≤t≤100) — количество наборов входных данных.
# Первая строка набора входных данных содержит два целых числа n и m (2≤n,m≤20) — кол-во строк и кол-во символов
# в каждой строке в описании карты. Далее следуют n строк по m символов в каждой — описание карты.
# 2 7
# G.B.R.G
# .G.G.G.
# - Выходные данные
# На каждый набор входных данных выведите ответ в отдельной строке — YES, если каждый регион карты представляет связную
# область, или NO, если это не так


# Returns a set of possible nearest points for a given point
def nearest_points(point):
    x = point[0]
    y = point[1]
    if y != 1 and x not in (1, 2):
        return {(x+2, y), (x-2, y), (x-1, y+1), (x+1, y+1), (x-1, y-1), (x+1, y-1)}
    elif y == 1 and x == 2:
        return {(x+2, y), (x-1, y+1), (x+1, y+1)}
    elif y == 1 and x == 1:
        return {(x+2, y), (x+1, y+1)}
    elif y != 1 and x == 2:
        return {(x+2, y), (x-1, y+1), (x+1, y+1), (x-1, y-1), (x+1, y-1)}
    elif y != 1 and x == 1:
        return {(x+2, y), (x+1, y+1), (x+1, y-1)}
    else:
        return {(x+2, y), (x-2, y), (x-1, y+1), (x+1, y+1)}


count = int(input())

for c in range(count):
    row_count, col_count = map(int, input().split())
    hex_coords_dict = {}
    for y in range(row_count, 0, -1):
        row = input()
        x = 1 if row[0] != '.' else 2
        for a in row.strip('.').split('.'):
            if hex_coords_dict.get(a):
                hex_coords_dict[a].append((x, y))
            else:
                hex_coords_dict[a] = [(x, y)]
            x += 2
    # print(hex_coords_dict)
    # {'G': [(1, 2), (7, 2), (2, 1), (4, 1), (6, 1)], 'B': [(3, 2)], 'R': [(5, 2)]}
    for hex_id, coords_list in hex_coords_dict.items():
        res = ''
        if len(coords_list) >= 2:
            hex_groups_set = [{coords_list[0]}]
            for coord in coords_list[1:]:
                near_points = nearest_points(coord)
                coord_added = False
                for group in hex_groups_set:
                    c_p = near_points & group
                    if c_p:
                        group.add(coord)
                        coord_added = True
                if not coord_added:
                    hex_groups_set.append({coord})
            # print(hex_groups_set)
            # [{(6, 1), (1, 2), (4, 1), (2, 1)}, {(6, 1), (7, 2)}, {...}]
            if len(hex_groups_set) >= 2:
                intersected_groups = set()
                for i, group in enumerate(hex_groups_set[:-1]):
                    for n, gr in enumerate(hex_groups_set[i+1:], i+1):
                        intersect = group & gr
                        if intersect:
                            intersected_groups.add(i)
                            intersected_groups.add(n)
                if len(intersected_groups) != len(hex_groups_set):
                    res = 'NO'
                    print(res)
                    break
    if not res:
        print('YES')
