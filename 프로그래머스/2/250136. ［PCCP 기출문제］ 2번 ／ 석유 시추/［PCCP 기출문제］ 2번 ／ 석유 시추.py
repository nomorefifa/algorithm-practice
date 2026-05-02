from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    
    # 각 열마다 얻을 수 있는 최종 석유량을 저장할 배열
    result_per_col = [0] * m
    visited = [[False] * m for _ in range(n)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        for j in range(m):
            # 방문하지 않은 석유 덩어리를 발견하면
            if land[i][j] == 1 and not visited[i][j]:
                # --- BFS 시작 ---
                q = deque([(i, j)])
                visited[i][j] = True
                
                size = 0 # 덩어리의 크기
                columns = set() # 덩어리가 걸쳐 있는 열 번호 (중복 제거)
                
                while q:
                    y, x = q.popleft()
                    size += 1
                    columns.add(x) # 현재 석유가 있는 '열' 번호 저장
                    
                    for k in range(4):
                        ny, nx = y + dy[k], x + dx[k]
                        if 0 <= ny < n and 0 <= nx < m:
                            if land[ny][nx] == 1 and not visited[ny][nx]:
                                visited[ny][nx] = True
                                q.append((ny, nx))
                
                # BFS가 끝나면 이 덩어리가 속한 모든 열에 크기를 더해줌
                for col in columns:
                    result_per_col[col] += size
                # --- BFS 끝 ---

    return max(result_per_col)