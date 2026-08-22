import sys
sys.setrecursionlimit(10000)
cnt = 0
def solution(numbers, target):
    def dfs(idx, val):
        global cnt
        if idx == len(numbers):
            if val == target:
                cnt += 1
            return
        dfs(idx + 1, val + numbers[idx])
        dfs(idx + 1, val - numbers[idx])
    dfs(0, 0)
    return cnt