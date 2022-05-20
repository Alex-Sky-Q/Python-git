import numpy as np

# Solve one of the following algorithmic tasks
# •	Transpose a matrix
matrix = np.array(
    [[1, 2, 6],
     [3, 16, 5]]
)


def transpose_matrix(matrix):
    res_matrix = []
    for i, row in enumerate(matrix):
        if i != 0:
            for ind, num in enumerate(row):
                res_matrix[ind].append(num)
        else:
            for num in row:
                res_matrix.append([num])
    return np.array(res_matrix)


# print(transpose_matrix(matrix))

# •	Turn a matrix on 90 degrees clockwise
matrix = np.array(
    [[1, 2, 5],
     [3, 10, 6],
     [5, 8, 3]]
)


def turn_matrix(matrix):
    res_matrix = np.zeros((len(matrix[0]),len(matrix)))
    for i in range(len(matrix[0])):
        for c in range(len(matrix)):
            res_matrix[i].put(c, matrix[len(matrix)-1-c][i])
    return res_matrix


print(turn_matrix(matrix))

# •	Multiply matrixes
matrixA = np.array(
    [[1, 2],
     [3, 10]]
)
matrixB = np.array(
    [[5, 2, 1],
     [6, 3, 2]]
)


def mult_matrix(matrA, matrB):
    if len(matrA[0]) == len(matrB):
        res_matrix = np.zeros((len(matrB), len(matrB[0])))
        for i, row in enumerate(matrA):
            for c in range(len(matrB[0])):
                sum_num = 0
                for ind in range(len(matrB)):
                    sum_num += row[ind] * matrB[ind][c]
                res_matrix[i].put(c, sum_num)
    else:
        res_matrix = 'A number of columns of the first matrix should be equal to a number of rows of the 2nd matrix'
    return res_matrix


# print(mult_matrix(matrixA, matrixB))

# •	Find a return matrix
# What does "return matrix" mean? Inverse matrix?

# •	Find a matrix determinant

# •	Find the second by length string in a list or array
string_list = ['one', 'search', 'begin', 'story', 'home']


def second_by_length(str_list):
    first_len = 0
    second_len = 0
    second_word = ''
    other_second_words = []
    for s in str_list:
        if len(s) > first_len:
            first_len = len(s)
        elif second_len < len(s) < first_len:
            second_len = len(s)
            second_word = s
        elif len(s) == second_len:
            other_second_words.append(s)

    print(f'The second by length word is "{second_word}" - {second_len} symbols')

    other_second_words_string = ''
    for i, w in enumerate(other_second_words):
        if i != (len(other_second_words) - 1):
            temp_string = w + ', '
        else:
            temp_string = w
        other_second_words_string += temp_string

    print(f'Other words with the same length are: "{other_second_words_string}"')


# second_by_length(string_list)

# •	Sort list or array by string length
string_list = ['tree', 'one', 'search', 'begin', 'story', 'home']


def sort_list(str_list):
    sorted_list = [str_list[0]]
    for s in str_list[1:]:
        for i, w in enumerate(sorted_list):
            if len(s) > len(w):
                sorted_list.insert(i, s)
                break
            elif i == (len(sorted_list) - 1):
                sorted_list.append(s)
                break
    return sorted_list


# print(sort_list(string_list))

# •	Sort list or array by count of vowels in string
string_list = ['one', 'search', 'begin', 'story', 'home', 'fifteen']


def count_vowels(word):
    vowels = 'aeiou'
    vowels_num = 0
    for el in word:
        if el in vowels:
            vowels_num += 1
    return vowels_num


def sort_by_vowels(str_list):
    sorted_list = [str_list[0]]
    for s in str_list[1:]:
        for i, w in enumerate(sorted_list):
            if count_vowels(s) > count_vowels(w):
                sorted_list.insert(i, s)
                break
            elif i == (len(sorted_list) - 1):
                sorted_list.append(s)
                break
    return sorted_list


# print(sort_by_vowels(string_list))

# •	Sort list or array by count of consonants in string
# Solution is the same as with vowels above. The only difference - consonants list instead of vowels list

# •	Change by places first and last letters in each second string of list or array
string_list = ['one', 'search', 'begin', 'story', 'home', 'fifteen']


def first_last(word):
    return word[-1] + word[1:-1] + word[0]


def fl_list(str_list):
    res_list = []
    for i, s in enumerate(str_list):
        if i % 2 != 0:
            s = first_last(s)
        res_list.append(s)
    return res_list


# print(fl_list(string_list))

# •	Revert strings of list or array
string_list = ['one', 'search', 'begin', 'story', 'home', 'fifteen']


def revert_string(word):
    # res = word[::-1] # built-in solution
    res = ''
    for w in word:
        res = w + res
    return res


def rv_str_list(str_list):
    return [revert_string(s) for s in str_list]

# print(rv_str_list(string_list))
