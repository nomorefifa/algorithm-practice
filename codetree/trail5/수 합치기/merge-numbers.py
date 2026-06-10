import heapq
n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
heapq.heapify(arr)
prefix_sum = 0
while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    prefix_sum += a + b
    heapq.heappush(arr, (a + b))
print(prefix_sum)