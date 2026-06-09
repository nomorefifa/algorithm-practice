n, m = map(int, input().split())
t = list(map(int, input().split()))

s = max(t)
e = sum(t)
ans = sum(t)
while s <= e:
    mid = (s + e) // 2
    cnt_line = 1
    cur_sum = 0
    for i in range(len(t)):
        if cur_sum + t[i] > mid:
            cnt_line += 1
            cur_sum = t[i]
        else:
            cur_sum += t[i]
    
    if cnt_line <= m:
        ans = mid
        e = mid - 1
    else:
        s = mid + 1
print(ans)