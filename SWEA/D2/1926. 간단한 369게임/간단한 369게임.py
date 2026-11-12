n = int(input())

for i in range(1, n + 1):
    str_num = str(i)
    cnt = 0

    for j in range(len(str_num)):
        for k in range(3, 10, 3):
            if str(k) == str_num[j]:
                cnt += 1

    if cnt:
        print('-' * cnt, end=" ")
    else:
        print(i, end=" ")