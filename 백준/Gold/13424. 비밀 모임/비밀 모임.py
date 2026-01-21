import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque
import heapq

INF = int(1e9)

def dijkstra(start):
    global ans
    q = []
    heapq.heappush(q, (0, start))
    min_weight[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if min_weight[node] < dist: continue
        for i in nlist[node]:
            cost = dist + i[1]
            if cost < min_weight[i[0]]:
                min_weight[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    for i in range(1, n + 1):
        ans[i] += min_weight[i]

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    nlist = [[] for _ in range(n + 1)]
    k_dict = {}
    for l in range(1, n + 1):
        k_dict[l] = 0
    for j in range(m):
        a, b, c = map(int, input().split())
        nlist[a].append((b, c))
        nlist[b].append((a, c))
    k = int(input())
    k_num = list(map(int, input().split()))
    ans = [0] * (n + 1)
    for start in k_num:
        min_weight = [INF] * (n + 1)
        dijkstra(start)
    min_cost = min(ans[1:])
    for i in range(1, n + 1):
        if ans[i] == min_cost:
            print(i)
            break