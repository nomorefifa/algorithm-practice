n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
i = 0 # a pointer
j = 0 # b pointer
while True:
    if b[j] == a[i]:
        j += 1
        i += 1
    else:
        i += 1
    
    if i >= n or j >= m:
        break

if j == m:
    print('Yes')
else:
    print('No')