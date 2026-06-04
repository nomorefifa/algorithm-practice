n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
dict = {}
ans = 0
end = 0
for start in range(n):
    while end < n:
        if arr[end] not in dict or dict[arr[end]] == 0:
            dict[arr[end]] = 1
            end += 1
        else:
            dict[arr[start]] -= 1
            break
    ans = max(ans, (end - start))
print(ans)