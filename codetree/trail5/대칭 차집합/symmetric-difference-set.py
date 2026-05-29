import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt_a = 0
cnt_b = 0
sa = set(A)
sb = set(B)
for i in range(m):
    if B[i] in sa:
        cnt_a += 1
for i in range(n):
    if A[i] in sb:
        cnt_b += 1
print((len(sa) - cnt_a) + (len(sb) - cnt_b))