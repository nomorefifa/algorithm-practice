import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
ngraph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    u, v = map(int, input().split())
    ngraph[u].append(v)
    ngraph[v].append(u)

def dfs(graph, start_node, visited):
    visited[start_node] = True
    for i in graph[start_node]:
        if not visited[i]:
            dfs(graph, i, visited)

cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(ngraph, i, visited)
        cnt += 1

print(cnt)