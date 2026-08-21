dict_words = []
vowels = ['A', 'E', 'I', 'O', 'U']

def recur(cur_word):
    if len(cur_word) != 5:
        for i in range(5):
            cur_word.append(vowels[i])
            dict_words.append("".join(cur_word))
            recur(cur_word)
            cur_word.pop()

def solution(word):
    ans = 0
    recur([])
    for i in range(len(dict_words)):
        if dict_words[i] == word:
            ans = i + 1
    return ans