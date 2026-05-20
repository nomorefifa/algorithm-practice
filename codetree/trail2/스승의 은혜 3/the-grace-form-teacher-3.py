N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
sum_arr = [gifts[i][0] + gifts[i][1] for i in range(N)]
ans = 0
for i in range(N):
    tmpCnt = 1
    tmpB = B - (gifts[i][0]) // 2 - gifts[i][1]
    tmpGifts = sorted(sum_arr[0:i] + sum_arr[i + 1:])
    for j in range(len(tmpGifts)):
        if tmpB - tmpGifts[j] >= 0:
            tmpB -= tmpGifts[j]
            tmpCnt += 1
    if tmpCnt > ans:
        ans = tmpCnt
print(ans)