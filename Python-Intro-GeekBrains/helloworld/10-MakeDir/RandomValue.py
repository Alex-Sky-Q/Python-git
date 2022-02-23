from random import choice


def rand_val(seq):
    if seq:
        rn = choice(seq)
        return rn


if __name__ == '__main__':
    test_list = []
    print(rand_val(test_list))
