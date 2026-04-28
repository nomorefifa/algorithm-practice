from itertools import permutations

def solution(numbers):
    numlist = list(numbers)
    set_num = set()
    cnt = 0
    for i in range(1, len(numlist) + 1):
        tmp = list(permutations(numlist, i))
        for j in range(len(tmp)):
            cur_num = ''
            for k in range(i):
                cur_num += tmp[j][k]
            cur_num = int(cur_num)
            set_num.add(cur_num)
    for num in set_num:
        if num < 2: continue
        flag = True
        for prime in range(2, num):
            if num % prime == 0:
                flag = False
                break
        if flag:
            cnt += 1
    return cnt