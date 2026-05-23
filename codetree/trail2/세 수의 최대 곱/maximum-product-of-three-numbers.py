n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()
case1 = arr[-1] * arr[-2] * arr[-3]

case2 = arr[0] * arr[1] * arr[-1]

print(max(case1, case2))