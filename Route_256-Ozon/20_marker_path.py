# В некоторую клетку прямоугольного поля была поставлена фишка. После этого был совершен один или более ход. Каждый ход
# фишку перемещали на соседнюю по стороне клетку вправо/влево/вверх или вниз. Известно, что фишка не посещала одну
# клетку дважды. Гарантируется, что любые две соседние по стороне посещенные клетки поля — это две последовательные
# клетки в пути фишки. Т.е. путь фишки не содержит самопересечений и самокасаний.
# Дано поле, на котором посещённые клетки отмечены символами '*' (звёздочка), а непосещённые — символами '.' (точка).
# Выведите любой возможный путь фишки в виде строки из букв 'R', 'L', 'U', 'D' (означающих перемещение
# вправо/влево/вверх/вниз соответственно). Путь фишки проходит исключительно по отмеченным клеткам и посещает все
# отмеченные клетки поля ровно по одному разу.
# - Входные данные
# В первой строке входных данных записано целое число t (1≤t≤100) — количество наборов входных данных в тесте.
# Наборы входных данных в тесте являются независимыми. Друг на друга они не влияют.
# Вторая строка содержит два целых числа n и m (1≤n,m≤100) — размеры поля. Гарантируется, что поле содержит хотя бы
# 2 клетки (то есть случай n=m=1 недопустим).
# Следующие n строк описывают поле. Каждая из них содержит m символов: точка ('.') либо звёздочка ('*'). Гарантируется,
# что все звёздочки образуют один путь фишки. Поле содержит хотя бы две звёздочки.
# 1
# 2 7
# .***...
# **.**..
# - Выходные данные
# Для каждого набора данных выведите любой из возможных путей фишки, кот. посетит по одному разу звёздочки и только их.
# Например: DDRRURRDD или UULLDLLUU.

# Returns a set of possible nearest points for a given point
def nearest_points(point):
    x = point[0]
    y = point[1]
    if y != 1 and x != 1:
        return {(x+1, y), (x-1, y), (x, y+1), (x, y-1)}
    elif y == 1 and x == 1:
        return {(x+1, y), (x, y+1)}
    elif y != 1 and x == 1:
        return {(x+1, y), (x, y+1), (x, y-1)}
    else:
        return {(x-1, y), (x+1, y), (x, y+1)}


def find_dir(curr_point, next_point):
    if next_point[0] == curr_point[0]:
        if next_point[1] > curr_point[1]:
            d = 'U'
        else:
            d = 'D'
    else:
        if next_point[0] > curr_point[0]:
            d = 'R'
        else:
            d = 'L'
    return d


def find_start(coords_list):
    for p in coords_list:
        near_points = nearest_points(p)
        intersect = set(coords_list) & near_points
        if len(intersect) == 1:
            return p


count = int(input())

for x in range(count):
    row_count, cols = map(int, input().split())
    coords_list = []
    for y in range(row_count, 0, -1):
        row = input()
        x = 1
        for a in row:
            if a == '*':
                coords_list.append((x, y))
            x += 1
    # print(coords_list)
    # [(1, 2), (5, 2), (6, 2), (7, 2), (3, 1), (6, 1), (7, 1)]
    res = []
    start_p = find_start(coords_list)
    coords_list = set(coords_list)
    for i in range(len(coords_list) - 1):
        if i == 0:
            near_points = nearest_points(start_p)
            intersect = coords_list & near_points
            res.append(find_dir(start_p, *intersect))
            next_p = list(intersect)[0]
            prev_p = start_p
        else:
            near_points = nearest_points(next_p)
            intersect = (coords_list & near_points) - {prev_p}
            res.append(find_dir(next_p, *intersect))
            prev_p = next_p
            next_p = list(intersect)[0]

    print(''.join(res))
