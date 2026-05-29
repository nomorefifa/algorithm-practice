import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
d = {}

for i in range(n):
    target = k - arr[i]
    if target in d:
        ans += d[target]
    if arr[i] in d:
        d[arr[i]] += 1
    else:
        d[arr[i]] = 1

print(ans)