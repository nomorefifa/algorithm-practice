import sys
sys.setrecursionlimit(2000)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        
        def dfs(node):
            # 1. 도시에 도착하자마자 방문 도장 쾅!
            visited[node] = True
            
            # 2. 내 도시(node)와 연결된 다른 도시(i)들을 0번부터 끝까지 쭉 훑어봄
            for i in range(n):
                # 3. 연결되어 있고(1), 아직 안 가본 도시라면 이동!
                if isConnected[node][i] == 1 and not visited[i]:
                    dfs(i)
                    
        cnt = 0
        
        # 4. 0번 도시부터 마지막 도시까지 순서대로 확인
        for i in range(n):
            # 5. 아직 안 가본 도시를 발견했다면? 새로운 지방(무리) 발견!
            if not visited[i]:
                cnt += 1  # 무리 개수 +1
                dfs(i)    # 이 도시와 연결된 모든 도시에 방문 도장 찍고 오라고 출발시킴
                
        return cnt