from collections import deque

def solution(maps):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    width = len(maps[0])
    height = len(maps)
    sol = []
    q = deque()
    visited = [[False] * (width) for _ in range(height)]
    for y in range(height):
        for x in range(width):
            cnt = 0
            if not visited[y][x] and maps[y][x] != "X":
                q.append((y, x))
                visited[y][x] = True
                cnt += int(maps[y][x])
                while q:
                    cur_y, cur_x = q.popleft()
                    for i in range(4):
                        next_y = cur_y + dy[i]
                        next_x = cur_x + dx[i]
                        if 0 <= next_y < height and 0 <= next_x < width:
                            if not visited[next_y][next_x] and maps[next_y][next_x] != "X":
                                cnt += int(maps[next_y][next_x])
                                visited[next_y][next_x] = True
                                q.append((next_y, next_x))
                if cnt > 0:
                    sol.append(cnt)
    sol.sort()
    if len(sol) > 0:
        return sol
    else:
        return [-1]