import sys
from collections import deque
input = sys.stdin.readline

r = [-1, 1, 0, 0]
c = [0, 0, -1, 1]

def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    while q:
        curr_y, curr_x = q.popleft()
        for i in range(4):
            next_y = curr_y + r[i]
            next_x = curr_x + c[i]
            if 0 <= next_y < row and 0 <= next_x < col:
                if not visited[next_y][next_x] and klist[next_y][next_x] == 1:
                    q.append((next_y, next_x))
                    visited[next_y][next_x] = True

t = int(input())
for i in range(t):
    col, row, k  = map(int, input().split())
    klist = [[0] * (col) for _ in range(row)]
    visited = [[False] * (col) for _ in range(row)]
    for j in range(k):
        x, y = map(int, input().split())
        klist[y][x] = 1
    
    cnt = 0
    for k in range(row):
        for l in range(col):
            if not visited[k][l] and klist[k][l] == 1:
                bfs(k, l)
                cnt += 1
    
    print(cnt)