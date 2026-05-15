n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0
for i in range(n):
    for j in range(n - 3 + 1):
        tmp = 0
        for k in range(3):
            if grid[i][j + k] == 1:
                tmp += 1
        if tmp > ans:
            ans = tmp
print(ans)