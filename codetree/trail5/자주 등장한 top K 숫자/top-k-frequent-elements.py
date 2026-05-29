n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
d = {}
for i in range(n):
    if arr[i] in d:
        d[arr[i]] += 1
    else:
        d[arr[i]] = 1
dlist = list(d.items())
sort_dlist = sorted(dlist, key = lambda x: (-x[1], -x[0]))

for i in range(k):
    print(sort_dlist[i][0], end = " ")