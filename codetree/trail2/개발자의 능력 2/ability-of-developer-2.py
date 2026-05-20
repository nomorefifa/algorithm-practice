ability = list(map(int, input().split()))

# Please write your code here.
total = sum(ability)
ans = 100000000000
for i in range(6):
    for j in range(i + 1, 6):
        for k in range(6):
            for l in range(k + 1, 6):
                if k == i or k == j or l == i or l == j:
                    continue
                t1 = ability[i] + ability[j]
                t2 = ability[k] + ability[l]
                t3 = total - t1 - t2
                if ans > max(t1, t2, t3) - min(t1, t2, t3):
                    ans = max(t1, t2, t3) - min(t1, t2, t3)
print(ans)