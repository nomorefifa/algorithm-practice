import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]

graph = [list(input().strip()) for _ in range(n)]
visited = [[False] * (m) for _ in range(n)]

q = deque()
q.append((0, 0, 1))
visited[0][0] = True

while q:
    curr_row, curr_col, dis = q.popleft()
    if curr_row == n - 1 and curr_col == m - 1:
        print(dis)
        break
    for i in range(4):
        next_row = curr_row + row[i]
        next_col = curr_col + col[i]

        if 0 <= next_row < n and 0 <= next_col < m:
            if visited[next_row][next_col] == False and int(graph[next_row][next_col]):
                visited[next_row][next_col] = True
                q.append((next_row, next_col, dis + 1))