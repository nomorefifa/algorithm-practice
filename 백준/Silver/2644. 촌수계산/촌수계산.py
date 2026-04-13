import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

node = int(input())
ans_x, ans_y = map(int, input().split())
edge = int(input())
visited = [False] * (node + 1)
graph = [[] for _ in range(node + 1)]

for i in range(edge):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(n, ans):
    if n == ans_y:
        print(ans)
        exit()
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i, ans + 1)

dfs(ans_x, 0)
print(-1)