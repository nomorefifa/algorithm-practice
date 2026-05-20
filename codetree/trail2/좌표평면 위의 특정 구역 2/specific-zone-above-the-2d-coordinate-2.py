n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
ans = 10000000000000000
for i in range(n):
    minx = min(x[0:i] + x[i + 1:])
    maxx = max(x[0:i] + x[i + 1:])
    miny = min(y[0:i] + y[i + 1:])
    maxy = max(y[0:i] + y[i + 1:])
    tmp = (maxx - minx) * (maxy - miny)
    if tmp < ans:
        ans = tmp
print(ans)