def solution(s):
    stack = []
    ans = True
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if stack:
                stack.pop()
            else:
                ans = False
                break
    if stack:
        ans = False
    return ans