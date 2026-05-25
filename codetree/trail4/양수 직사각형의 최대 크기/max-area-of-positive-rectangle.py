n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0
for i in range(n):
    for j in range(m): # 시작점 (i, j)
        for k in range(n):
            if k < i:
                continue
            for l in range(m): # 끝점(k, l)
                if l < j:
                    continue
                cnt = 0
                for row in range(i, k + 1):
                    for col in range(j, l + 1):
                        if grid[row][col] > 0:
                            cnt += 1
                if cnt == (k - i + 1) * (l - j + 1):
                    if cnt > ans:
                        ans = cnt

if ans:
    print(ans)
else:
    print(-1)