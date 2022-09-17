# 1
# 6
# 10 -1 x
# 20 10 x
# 40 -1 x
# 50 -1 x
# 11 20 x
# 30 10 x
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

count = int(input())

for x in range(count):
    comm_total = int(input())
    comm_list = []
    for c in range(comm_total):
        comm_id, par_id, comm_text = input().split(maxsplit=2, sep=' ')
        comm_list.append((int(comm_id), int(par_id), comm_text))

    base_comments = [c[0] for c in comm_list if c[1] == -1]
print(base_comments)


def sort_comments(from_list):
    pass

