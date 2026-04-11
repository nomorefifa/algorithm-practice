from collections import deque

n = int(input())
nlist = deque([i for i in range(n, 0, -1)])
if n == 1:
    print(1)
    exit()
while True:
    nlist.pop()
    if len(nlist) == 1:
        print(nlist[0])
        break
    nlist.appendleft(nlist.pop())