n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(n):
    tmp = [0] * (101)
    for j in range(n):
        if i == j:
            continue
        for k in range(segments[j][0], segments[j][1] + 1):
            tmp[k] += 1
            if tmp[k] >= n - 1:
                print('Yes')
                exit(0)
print('No')