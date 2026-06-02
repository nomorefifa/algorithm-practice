n, q = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
larr = [0] * (n + 1)
rarr = [0] * (n) + [arr[-1]]

for i in range(1, n + 1):
    larr[i] = max(larr[i - 1], arr[i - 1])

for i in range(n - 1, 0, -1):
    rarr[i] = max(rarr[i + 1], arr[i - 1])

for i in range(q):
    print(max(larr[queries[i][0] - 1], rarr[queries[i][1] + 1]))