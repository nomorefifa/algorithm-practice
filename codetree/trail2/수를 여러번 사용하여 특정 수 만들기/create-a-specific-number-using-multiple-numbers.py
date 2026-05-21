a, b, c = map(int, input().split())

ans = 0
for i in range(c // a + 2):
    for j in range(c // b + 2):
        tmp = a * i + b * j
        if tmp <= c:
            if ans  < tmp:
                ans = tmp
print(ans)