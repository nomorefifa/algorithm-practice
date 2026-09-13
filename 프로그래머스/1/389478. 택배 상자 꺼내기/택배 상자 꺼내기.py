def solution(n, w, num):
    if n % w == 0:
        h = n // w
    else:
        h = (n // w) + 1
    grid = [[0] * (w) for _ in range(h)]
    cnt = 1
    flag = 1 #1은 정방향, -1은 역방향
    for row in range(h - 1, -1, -1):
        for col in range(w):
            if flag == 1:
                grid[row][col] = cnt
            else:
                grid[row][(w - 1) - col] = cnt
            cnt += 1
            if cnt == n + 1:
                break
        flag *= -1
    target_col = 0
    target_row = 0
    if num % w == 0:
        target_row = h - (num // w)
    else:
        target_row = (h - 1) - num // w
    for i in range(w):
        if grid[target_row][i] == num:
            target_col = i
    ans = 0
    #print(grid[target_row][target_col])
    for i in range(h):
        if grid[i][target_col] != 0 and grid[i][target_col] >= num:
            ans += 1
    return ans