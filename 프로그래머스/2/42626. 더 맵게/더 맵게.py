import heapq

def solution(scoville, k):
    ans = 0
    q = []
    for i in range(len(scoville)):
        heapq.heappush(q, scoville[i])
    while len(q) >= 2:
        tmp1 = heapq.heappop(q)
        if tmp1 >= k:
            break
        tmp2 = heapq.heappop(q)
        heapq.heappush(q, tmp1 + tmp2 * 2)
        ans += 1
    if heapq.heappop(q) < k:
        ans = -1
    return ans