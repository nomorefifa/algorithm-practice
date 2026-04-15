import sys
from collections import deque
input = sys.stdin.readline

n_dir = [0, 0, -1, 1, 0, 0]
m_dir = [0, 0, 0, 0, -1, 1]
h_dir = [1, -1, 0, 0, 0, 0]

m, n, h = map(int, input().split())
graph = []
for i in range(h):
    graph.append([list(map(int, input().split())) for _ in range(n)])

q = deque()
one_cnt = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i, j, k))
                one_cnt += 1

while q:
    curr_h, curr_n, curr_m = q.popleft()
    for i in range(6):
        next_h = curr_h + h_dir[i]
        next_n = curr_n + n_dir[i]
        next_m = curr_m + m_dir[i]
        if 0 <= next_h < h and 0 <= next_n < n and 0 <= next_m < m:
            if graph[next_h][next_n][next_m] == 0:
                graph[next_h][next_n][next_m] += graph[curr_h][curr_n][curr_m] + 1
                q.append((next_h, next_n, next_m))

max = -2
minus_cnt = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == -1:
                minus_cnt += 1
            elif graph[i][j][k] == 0:
                print(-1)
                exit()
            else:
                if graph[i][j][k] > max:
                    max = graph[i][j][k]

if one_cnt + minus_cnt == h * n * m:
    print(0)
else:
    print(max - 1)