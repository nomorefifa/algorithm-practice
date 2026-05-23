n = int(input())
nlist = list(map(int, input().split()))

nlist.sort()
pos = 0
zero = 0
neg = 0
for i in range(n):
    if nlist[i] > 0:
        pos += 1
    elif nlist[i] == 0:
        zero += 1
    else:
        neg += 1

ans = 0
if pos >= 3 or (pos == 1 and neg >= 2):
    ans = max(nlist[n-1] * nlist[n-2] * nlist[n-3], nlist[n-1] * nlist[0] * nlist[1])
elif zero >= 1:
    ans = 0
else:
    ans = nlist[n-1] * nlist[n-2] * nlist[n-3]

print(ans)