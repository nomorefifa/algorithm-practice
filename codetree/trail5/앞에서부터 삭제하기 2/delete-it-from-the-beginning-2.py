import heapq
n = int(input())
nlist = list(map(int, input().split()))

hq = []
ans = 0
heapq.heappush(hq, nlist[-1])
cur_sum = nlist[-1]
for i in range(n - 2, 0, -1):
    heapq.heappush(hq, nlist[i])
    cur_sum += nlist[i]
    avg = (cur_sum - hq[0]) / (len(hq) - 1)
    if avg > ans:
        ans = avg
print(f"{ans:.2f}")