n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
top3 = []
for i in range(n):
    top3.append(arr[i])
    if len(top3) < 3:
        print(-1)
    else:
        top3.sort()
        top3 = top3[:3]
        mul = 1
        for j in range(3):
            mul *= top3[j]
        print(mul)