from collections import deque
import sys
sys.setrecursionlimit(10000)
imput = sys.stdin.readline

node, edge, start_node = map(int, input().split())
graph = [[] for _ in range(node + 1)]

for i in range(edge):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, node + 1):
    graph[i].sort()

dfs_ans = []
def dfs(n):
    visited[n] = True
    dfs_ans.append(str(n))
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

bfs_ans = []
def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = True
    while q:
        curr_node = q.popleft()
        bfs_ans.append(str(curr_node))
        for i in graph[curr_node]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

visited = [False] * (node + 1)
dfs(start_node)
visited = [False] * (node + 1)
bfs(start_node)
print(" ".join(dfs_ans))
print(" ".join(bfs_ans))