n, q = map(int, input().split())
points = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
dict = {}
cnt = 1
for i in range(n):
    dict[points[i]] = cnt
    cnt += 1

for i in range(q):
    print(dict[queries[i][1]] - dict[queries[i][0]] + 1)