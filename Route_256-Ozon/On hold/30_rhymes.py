# Вы разрабатываете программу автоматической генерации стихотворений. Один из модулей этой программы должен подбирать
# рифмы к словам из некоторого словаря. Словарь содержит n различных слов. Словами будем называть последовательности из
# 1—10 строчных букв латинского алфавита. Зарифмованность двух слов — это длина их наибольшего общего суффикса
# (суффиксом будем называть какое-то количество букв в конце слова). Например:
# task и flask имеют зарифмованность 3 (наибольший общий суффикс — ask);
# decide и code имеют зарифмованность 2 (наибольший общий суффикс — de);
# id и void имеют зарифмованность 2 (наибольший общий суффикс — id);
# code и forces имеют зарифмованность 0.
# Ваша программа должна обработать q запросов следующего вида: дано слово ti (возможно, принадлежащее словарю),
# необходимо найти слово из словаря, которое не совпадает с ti и имеет максимальную зарифмованность с ti среди всех слов
# словаря, не совпадающих с ti. Если подходящих слов несколько — выведите любое из них.
# - Входные данные
# Первая строка содержит одно целое число n (2≤n≤50000) — размер словаря.
# Далее идут n строк, i-я строка содержит 1 строку si (1≤|si|≤10) — i-е слово из словаря. В словаре все слова различны
# Следующая строка содержит одно целое число q (1≤q≤50000) — количество запросов.
# Далее следуют q строк, i-я строка содержит одну строку ti (1≤|ti|≤10) — i-й запрос.
# Каждая строка si и каждая строка ti состоит только из строчных букв латинского алфавита.
# - Выходные данные
# Для каждого запроса выведите одну строку — слово из словаря, которое не совпадает с заданным в запросе и имеет с ним
# максимальную зарифмованность (если таких несколько — выведите любое).
# 3
# task
# decide
# id
# 6
# flask
# code
# void
# forces
# id
# ask

dict_size = int(input())
word_dict = {}
# zero_word = ''
for i in range(dict_size):
    word = input()
    if word_dict.get(word[-1]):
        word_dict[word[-1]].append(word)
    else:
        word_dict[word[-1]] = [word]


def find_max_rhyme(word):
    max_rhyme = 0
    res = ''
    inds = []
    words = word_dict.get(word[-1])
    for i, w in enumerate(words):
        res = w
    return res


queries_size = int(input())
for i in range(queries_size):
    word = input()
    if not word_dict.get(word[-1]):
        print(*next(word for word in word_dict.values()))
    else:
        print(find_max_rhyme(word))
