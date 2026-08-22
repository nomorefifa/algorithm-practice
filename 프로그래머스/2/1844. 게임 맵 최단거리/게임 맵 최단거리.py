from collections import deque
dir_row = [-1, 1, 0, 0]
dir_col = [0, 0, -1, 1]
def solution(maps):
    q = deque()
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    q.append([0, 0])
    visited[0][0] = 1
    #maps[0] -> col, maps -> row
    def bfs():
        while q:
            cur_row, cur_col = q.popleft()
            for i in range(4):
                next_row = cur_row + dir_row[i]
                next_col = cur_col + dir_col[i]
                if 0 <= next_row < len(maps) and 0 <= next_col < len(maps[0]):
                    if not visited[next_row][next_col] and maps[next_row][next_col] == 1:
                        q.append([next_row, next_col])
                        visited[next_row][next_col] += visited[cur_row][cur_col] + 1
    ans = bfs()
    if visited[len(maps) - 1][len(maps[0]) - 1] == 0:
        return - 1
    else:
        return visited[len(maps) - 1][len(maps[0]) - 1]