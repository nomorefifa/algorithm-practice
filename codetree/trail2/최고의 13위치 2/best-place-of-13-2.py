n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0
for i in range(n):
    for j in range(n - 3 + 1):
        tmp1 = sum(arr[i][j:j + 3])
        for k in range(n):
            for l in range(n - 3 + 1):
                if i == k and abs(j - l) < 3: # 두개가 같은 행일경우
                    continue
                tmp2 = sum(arr[k][l:l + 3])
                if tmp1 + tmp2 > ans:
                    ans = tmp1 + tmp2
print(ans)