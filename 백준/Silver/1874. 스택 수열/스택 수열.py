n = int(input())
nlist = []
for i in range(n):
    num = int(input())
    nlist.append(num)

ans = []
num = 1
num_list = []
for i in range(n):
    while True:
        if nlist[i] >= num:
            num_list.append(num)
            num += 1
            ans.append('+')
        else:
            if num_list.pop() == nlist[i]:
                ans.append('-')
                break
            else:
                print("NO")
                exit()
for i in ans:
    print(i)