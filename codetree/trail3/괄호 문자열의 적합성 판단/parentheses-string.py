str = input()

# Please write your code here.
stack = []
for i in range(len(str)):
    if str[i] == '(':
        stack.append('(')
    else:
        if stack:
            stack.pop()
        else:
            print('No')
            exit(0)
if len(stack) == 0:
    print('Yes')
else:
    print('No')