# Solve one of the following algorithmic tasks
# •	Transpose a matrix
# •	Turn a matrix on 90 degrees clockwise
# •	Multiply matrixes
# •	Find a return matrix
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


# •	Revert strings of list or array
