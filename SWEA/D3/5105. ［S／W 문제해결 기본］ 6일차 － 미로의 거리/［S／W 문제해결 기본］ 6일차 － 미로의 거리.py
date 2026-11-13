from collections import deque
dir_row = [-1, 1, 0, 0]
dir_col = [0, 0, -1, 1]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    nlist = [list(input()) for _ in range(n)]
    visited = [[False] * (n) for _ in range(n)]
    q = deque()
    s_row = 0
    s_col = 0
    for i in range(n):
        for j in range(n):
            if nlist[i][j] == "2":
                s_row = i
                s_col = j
    
    visited[s_row][s_col] = True
    cnt = 0
    ans = 0
    flag = False
    q.append((s_row, s_col, cnt))
    while q:
        cur_row, cur_col, cnt = q.popleft()
        if nlist[cur_row][cur_col] == "3":
            flag = True
            ans = cnt
            break
        for i in range(4):
            next_row = cur_row + dir_row[i]
            next_col = cur_col + dir_col[i]
            if 0 <= next_row < n and 0 <= next_col < n and not visited[next_row][next_col] and nlist[next_row][next_col] != "1":
                q.append((next_row, next_col, cnt + 1))
                visited[next_row][next_col] = True
    if flag:
        print(f"#{test_case} {ans - 1}")
    else:
        print(f"#{test_case} 0")
    # ///////////////////////////////////////////////////////////////////////////////////
