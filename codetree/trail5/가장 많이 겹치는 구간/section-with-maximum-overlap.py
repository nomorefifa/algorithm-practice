n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
x = [0] * (200001)

for i in range(n):
    x[intervals[i][0]] += 1
    x[intervals[i][1]] -= 1

s = [0] * (200001)
for i in range(1, 200001):
    s[i] = s[i - 1] + x[i]

print(max(s))