n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()
ans = float(1e9)
for i in range(n):
    if arr[i + n] - arr[i] < ans:
        ans = arr[i + n] - arr[i]
print(ans)