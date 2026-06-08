from bisect import bisect_right, bisect_left
n, m = map(int, input().split())
points = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
points.sort()

for s, e in segments:
    print(bisect_right(points, e) - bisect_left(points, s))