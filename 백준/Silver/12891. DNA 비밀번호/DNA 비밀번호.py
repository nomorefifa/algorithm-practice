import sys
input = sys.stdin.readline

s, p = map(int, input().split())
pw = list(input())
con = list(map(int, input().split()))

cnt = 0
ans = {'A':0, 'C':0, 'G':0, 'T':0}
for i in range(p):
    ans[pw[i]] += 1

if ans['A'] >= con[0] and ans['C'] >= con[1] and ans['G'] >= con[2] and ans['T'] >= con[3]:
       cnt += 1

for i in range(p, s):
    ans[pw[i - p]] -= 1
    ans[pw[i]] += 1
    if ans['A'] >= con[0] and ans['C'] >= con[1] and ans['G'] >= con[2] and ans['T'] >= con[3]:
       cnt += 1

print(cnt)