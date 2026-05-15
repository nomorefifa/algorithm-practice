N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
ans = 100000000000
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        tmp = sum(arr) - arr[i] - arr[j]
        if abs(S - tmp) < ans:
            ans = abs(S - tmp)

print(ans)