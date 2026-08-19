from itertools import permutations

def isprime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    visited = [False] * len(numbers)
    prime_set = set()
    def dfs(num):
        for i in range(len(numbers)):
            if visited[i] == True:
                continue
            visited[i] = True
            cur_num = num * 10 + int(numbers[i])
            if isprime(cur_num):
                prime_set.add(cur_num)
            dfs(cur_num)
            visited[i] = False
    dfs(0)
    return len(prime_set)