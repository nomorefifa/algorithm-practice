import sys
import heapq
input = sys.stdin.readline
n, k = map(int, input().split())

hq = [[] for _ in range(12)]
pos = [-1] * (12)
for i in range(n):
    p, w = map(int, input().split())
    heapq.heappush(hq[p], -w)

for i in range(k):
    for j in range(1, 12):
        if len(hq[j]):
            if pos[j] < -hq[j][0]:
                tmp = pos[j]
                pos[j] = -(heapq.heappop(hq[j]))
                heapq.heappush(hq[j], -tmp)
    for j in range(1, 12):
        if pos[j] != -1 and pos[j] != 0:
            pos[j] -= 1
    for j in range(1, 12):
        if len(hq[j]):
            if pos[j] < -hq[j][0]:
                tmp = pos[j]
                pos[j] = -(heapq.heappop(hq[j]))
                heapq.heappush(hq[j], -tmp)
ans = 0
for i in range(1, 12):
    if pos[i] != -1:
        ans += pos[i]
print(ans)