n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
ans = 0
cur_sum = 0
for i in range(n):
    if cur_sum + a[i] < 0:
        cur_sum = 0
    else:
        cur_sum += a[i]
        ans = max(ans, cur_sum)

if ans == 0:
    print(max(a))
else:
    print(ans)