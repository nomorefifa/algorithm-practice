N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
ans = 100000000
for i in range(N - T + 1):
    tmp = 0
    for j in range(T):
        tmp += abs(H - arr[i + j])
    if tmp < ans:
        ans = tmp

print(ans)