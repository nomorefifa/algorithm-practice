n, k = map(int, input().split())
arr = list(map(int, input().split()))

s = 0
e = 0
cnt = 0
ans = float('1e9')
while e < n:
    if arr[e] == 1:
        cnt += 1
    while cnt == k:
        ans = min(ans, (e - s + 1))
        if arr[s] == 1:
            cnt -= 1
        s += 1
    e += 1
if ans == float('1e9'):
    print(-1)
else:
    print(ans)