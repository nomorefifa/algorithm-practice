import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
sort_nlist = sorted(nlist)

cnt = 0
for i in range(n):
    num = sort_nlist[i]
    s = 0
    e = n - 1
    while s != e:
        tmp_sum = sort_nlist[s] + sort_nlist[e]

        if tmp_sum < num:
            s += 1
        elif tmp_sum > num:
            e -= 1
        else:
            if s == i:
                s += 1
            elif e == i:
                e -= 1
            else:
                cnt += 1
                break

print(cnt)