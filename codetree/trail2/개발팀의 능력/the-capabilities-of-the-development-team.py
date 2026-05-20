arr = list(map(int, input().split()))

# Please write your code here.
total = sum(arr)
flag = False
ans = 1000000000000
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(5):
            if k == i or k == j:
                continue
            t1 = arr[i] + arr[j]
            t2 = arr[k] # alone
            t3 = total - t1 - t2
            if t1 == t2 or t2 == t3 or t1 == t3:
                continue
            if t1 != t2 and t2 != t3 and t1 != t3:
                flag = True
            if ans > max(t1, t2, t3) - min(t1, t2, t3):
                ans = max(t1, t2, t3) - min(t1, t2, t3)
if flag:
    print(ans)
else:
    print(-1)