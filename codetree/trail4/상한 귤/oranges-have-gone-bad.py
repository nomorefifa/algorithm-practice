from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]

q = deque()
ans = [[-2] * (n) for _ in range(n)]
visited = [[False] * (n) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            q.append((i, j))
            visited[i][j] = True
            ans[i][j] = 0
        if grid[i][j] == 0:
            ans[i][j] = -1

time = 1
while q:
    round = len(q)
    for i in range(round):
        cur_row, cur_col = q.popleft()
        visited[cur_row][cur_col] = True
        for j in range(4):
            next_row = cur_row + row[j]
            next_col = cur_col + col[j]
            if 0 <= next_row < n and 0 <= next_col < n and not visited[next_row][next_col]:
                visited[next_row][next_col] = True
                if grid[next_row][next_col] == 1:
                    ans[next_row][next_col] = time
                    q.append((next_row, next_col))
    time += 1

for i in range(n):
    for j in range(n):
        print(ans[i][j], end = ' ')
    print()