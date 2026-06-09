n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# Please write your code here.
ans = 0
cur_cost = k
for i in range(n - 1, -1, -1):
    ans += cur_cost // coins[i]
    cur_cost = cur_cost % coins[i]

for i in range(n):
    if k % coins[i] == 0 and k //coins[i] < ans:
        ans = k //coins

print(ans)