a = input()

# Please write your code here.
ans = float('1e9')
for i in range(len(a)):
    cur_word = a[-1] + a[:len(a) - 1]
    a = cur_word
    ans_word = ""
    pre = a[0]
    ans_word += pre
    cnt = 1
    for j in range(1, len(a)):
        if a[j] != pre:
            ans_word += str(cnt)
            ans_word += a[j]
            cnt = 1
        else:
            cnt += 1
        pre = a[j]
    ans_word += str(cnt)
    if len(ans_word) < ans:
        ans = len(ans_word)

print(ans)