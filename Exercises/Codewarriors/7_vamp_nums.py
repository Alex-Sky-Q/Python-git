def gen_nums(vamp_len):
    vamps = []
    start, stop = 10 ** vamp_len, 10 ** (vamp_len + 1)
    for a in range(start, stop):
        for b in range(a, stop):
            prod = a * b
            m1 = str(a)
            m2 = str(b)
            if m1[-1] == '0' and m2[-1] == '0':
                continue
            if sorted(str(prod)) == sorted(m1 + m2):
                vamps.append(prod)
    return vamps


def vampire_number(k):
    vamps = []
    for vamp_len in range(1, 3):
        vamps.extend(gen_nums(vamp_len))
        if len(vamps) >= k:
            break
    vamps = list(set(vamps))
    vamps.sort()
    return vamps[k-1]
    