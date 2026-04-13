import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

node = int(input())
edge = int(input())
visited = [False] * (node + 1)
graph = [[] for _ in range(node + 1)]

for i in range(edge):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 0
def dfs(n):
    global cnt
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)