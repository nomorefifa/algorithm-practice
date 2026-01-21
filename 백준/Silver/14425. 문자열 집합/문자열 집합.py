import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

s = set()
n, m = map(int, input().split())

for i in range(n):
    str = input()
    s.add(str)

cnt = 0

for i in range(m):
    str = input()
    if str in s:
        cnt += 1

print(cnt)