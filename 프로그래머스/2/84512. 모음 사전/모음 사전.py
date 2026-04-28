from itertools import product

def solution(word):
    shit = ['A','E', 'I','O','U']
    word_list = set()
    for i in range(1, 6):
        for j in product(shit, repeat = i):
            word_list.add(''.join(j))
    word_list = list(word_list)
    word_list.sort()
    return word_list.index(word) + 1