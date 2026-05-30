n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import heapq
hq = []

for i in range(n):
    heapq.heappush(hq, (points[i][0] + points[i][1], points[i][0], points[i][1]))
    #hq에 (x+y, x, y) 형태로 넣기

for i in range(m):
    s, x, y = heapq.heappop(hq)
    x += 2
    y += 2
    heapq.heappush(hq, (x + y, x, y))

s, ansx, ansy = heapq.heappop(hq)
print(ansx, ansy)