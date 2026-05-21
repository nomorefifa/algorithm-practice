x, y = map(int, input().split())

cnt = 0
for num in range(x, y + 1):
    flag = True
    word = str(num)
    for i in range(len(word) // 2):
        if word[i] != word[(len(word)) - 1 - i]:
            flag = False
            break
    if flag:
        cnt += 1
print(cnt)