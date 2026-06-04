n, s = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
start = 0
end = 0
tmp_sum = 0
ans = n + 1
flag = False
while start < n:
    while end < n and tmp_sum < s:
        tmp_sum += arr[end]
        end += 1
    if tmp_sum >= s:
        ans = min(ans, (end - start))
        flag = True
    tmp_sum -= arr[start]
    start += 1

if flag:
    print(ans)
else:
    print(-1)