import sys
sys.setrecursionlimit(2000)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * (len(isConnected))
        graph = [[] for _ in range(len(isConnected))]
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        def dfs(node):
            visited[node] = True
            for next_node in graph[node]:
                if not visited[next_node]:
                    dfs(next_node)
        cnt = 0
        for i in range(len(graph)):
            if not visited[i]:
                cnt += 1
                dfs(i)
        
        return cnt