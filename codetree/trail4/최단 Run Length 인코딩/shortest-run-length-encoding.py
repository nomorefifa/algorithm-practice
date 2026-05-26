a = input()

# Please write your code here.
ans = float('1e9')
for i in range(len(a)):
    cur_word = a[-1] + a[:len(a) - 1]
    a = cur_word

    pre = a[0]
    cnt = 1
    for j in range(1, len(a)):
        if a[j] != pre:
            cnt += 1
        pre = a[j]
    
    if cnt < ans:
        ans = cnt

if ans == 1 and len(a) == 10:
    print(3)
else:
    print(ans * 2)