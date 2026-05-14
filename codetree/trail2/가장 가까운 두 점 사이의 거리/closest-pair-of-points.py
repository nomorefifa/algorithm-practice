n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
ans = 100000000000
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        tmp = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
        if tmp < ans:
            ans = tmp
print(ans)