n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
sort_meet = sorted(meetings, key = lambda x: x[1])
cnt = 1
cur_time = sort_meet[0][1]
for i in range(1, n):
    if sort_meet[i][0] >= cur_time:
        cur_time = sort_meet[i][1]
        cnt += 1
    else:
        continue
print(cnt)