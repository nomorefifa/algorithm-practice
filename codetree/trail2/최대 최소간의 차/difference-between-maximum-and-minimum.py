n, k = map(int, input().split())
arr = list(map(int, input().split()))

start_min = min(arr)
start_max = max(arr)

ans = float('inf')
for i in range(start_min, start_max - k + 1):
    cur_min = i
    cur_max = i + k
    cnt = 0
    for j in range(n):
        if arr[j] < cur_min:
            cnt += (cur_min - arr[j])
        if arr[j] > cur_max:
            cnt += (arr[j] - cur_max)
    if cnt < ans:
        ans = cnt
print(ans)