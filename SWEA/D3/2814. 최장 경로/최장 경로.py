def dfs(node, cnt):
    global ans
    if cnt > ans:
        ans = cnt
    for next_node in nlist[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, cnt + 1)
            visited[next_node] = False

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split()) # 정점=n, 간선=m
    nlist = [[] for _ in range(n + 1)]
    for i in range(m):
        x, y = map(int, input().split())
        nlist[x].append(y)
        nlist[y].append(x)
    ans = 0 # 최대 정점수
    for i in range(1, n + 1):
        visited = [False] * (n + 1)
        dfs(i, 0)
    print(f"#{test_case} {ans}")