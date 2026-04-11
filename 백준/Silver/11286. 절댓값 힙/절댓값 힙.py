import sys
import heapq 
input = sys.stdin.readline

n = int(input())
hq = []
for i in range(n):
    info = int(input())
    if info == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq)[1])
    else:
        heapq.heappush(hq, (abs(info), info))