n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
x1 = [i[0] for i in segments]
x2 = [i[1] for i in segments]
ans = float(1e9)
for i in range(n):
    if max(x2[:i] + x2[i + 1:]) - min(x1[:i] + x1[i + 1:]) < ans:
        ans = max(x2[:i] + x2[i + 1:]) - min(x1[:i] + x1[i + 1:])
print(ans)