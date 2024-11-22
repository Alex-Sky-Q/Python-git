def pascal_row(n):
    num = 1
    res = [num]
    for i in range(1, n):
        # formula to generate Pascal's triangle row elements
        num = round(num * (n / i))
        n -= 1
        res.append(num)
    return res
