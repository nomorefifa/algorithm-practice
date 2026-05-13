import sys
sys.setrecursionlimit(20000)

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * (len(rooms))
        def dfs(node):
            visited[node] = True
            for j in rooms[node]:
                if not visited[j]:
                    dfs(j)
        dfs(0)
        flag = True
        for i in range(len(rooms)):
            if visited[i] == True:
                continue
            else:
                flag = False
                break
        return flag