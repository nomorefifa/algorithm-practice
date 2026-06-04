n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
ans = -1
dict = {}
for i in range(n):
    if arr[i] in dict:
        if (i - dict[arr[i]]) <= k:
            if arr[i] > ans:
                ans = arr[i]
            dict[arr[i]] = i
    else:
        dict[arr[i]] = i

print(ans)