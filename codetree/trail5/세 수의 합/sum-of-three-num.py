n, k = map(int, input().split())
nlist = list(map(int, input().split()))

ans = 0
for i in range(n - 2):
    target = k - nlist[i]
    d = {}
    for j in range(i + 1, n):
        rest = target - nlist[j]
        if rest in d:
            ans += d[rest]
        if nlist[j] in d:
            d[nlist[j]] += 1
        else:
            d[nlist[j]] = 1

print(ans)