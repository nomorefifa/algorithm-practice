N, Q = map(int, input().split())
arr = [int(input()) for _ in range(N)]
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# Please write your code here.
one = [0] * (N + 1)
two = [0] * (N + 1)
three = [0] * (N + 1)

for i in range(N):
    if arr[i] == 1:
        one[i + 1] = 1
    elif arr[i] == 2:
        two[i + 1] = 1
    else:
        three[i + 1] = 1

for i in range(2, N + 1):
    one[i] += one[i - 1]
    two[i] += two[i - 1]
    three[i] += three[i - 1]

for i in range(Q):
    tmp1 = 0
    tmp2 = 0
    tmp3 = 0
    tmp1 += (one[queries[i][1]] - one[queries[i][0] - 1])
    tmp2 += (two[queries[i][1]] - two[queries[i][0] - 1])
    tmp3 += (three[queries[i][1]] - three[queries[i][0] - 1])
    print(tmp1, tmp2, tmp3)