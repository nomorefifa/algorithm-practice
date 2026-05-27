n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]
visited = [[False]  * (n) for _ in range(n)]

# 4개 이상 터짐, 터지는 블럭 개수 / 가장 큰 블럭 개수
cnt = 0
big = 0
def dfs(dy, dx, num):
    global tmp
    visited[dy][dx] = True
    for i in range(4):
        next_row = dy + row[i]
        next_col = dx + col[i]
        if 0 <= next_row < n and 0 <= next_col < n:
            if not visited[next_row][next_col] and grid[next_row][next_col] == num:
                tmp += 1
                dfs(next_row, next_col, num)

for i in range(n):
    for j in range(n):
        tmp = 1
        if not visited[i][j]:
            cur_num = grid[i][j]
            dfs(i, j, cur_num)
            if tmp >= 4:
                cnt += 1
            if tmp > big:
                big = tmp

print(cnt, big)