import sys
input = sys.stdin.readline

n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

ci = []
for i in range(n):
    ci.append((intervals[i][0], 1))
    ci.append((intervals[i][1] + 1, -1))

ans = 0
cur = 0
ci.sort()
for i in range(n):
    cur += ci[i][1]
    if cur > ans:
        ans = cur
print(ans)