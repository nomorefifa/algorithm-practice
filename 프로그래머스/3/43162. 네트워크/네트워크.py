import sys
sys.setrecursionlimit(10**6)

def solution(n, computers):
    node_cnt = len(computers) # 노드개수
    graph = [[] for _ in range(node_cnt)]
    visited = [False] * (node_cnt)
    ans = 0
    for i in range(node_cnt): # 연결된 그래프 상태 채우기
        for j in range(node_cnt):
            if i == j:
                continue
            if computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
    def dfs(node):
        visited[node] = True
        for next_node in graph[node]:
            if not visited[next_node]:
                dfs(next_node)
    for i in range(node_cnt):
        if not visited[i]:
            dfs(i)
            ans += 1
    return ans