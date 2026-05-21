n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
ans = 0
for i in range(1, n + 1):
    tmp_sum = 0
    cur_idx = i
    for j in range(m):
        tmp_sum += arr[cur_idx]
        cur_idx = arr[cur_idx]
    if tmp_sum > ans:
        ans = tmp_sum

print(ans)