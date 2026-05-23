n = int(input())
arr = list(input().split())

# Please write your code here.
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] > arr[j]:
            ans += 1

print(ans)