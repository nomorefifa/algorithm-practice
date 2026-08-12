def solution(prices):
    ans = [0] * (len(prices))
    idx_stack = [0]
    for i in range(1, len(prices)):
        if idx_stack:
            if prices[idx_stack[-1]] > prices[i]:
                while idx_stack and prices[idx_stack[-1]] > prices[i]:
                    ans[idx_stack[-1]] = i - idx_stack[-1]
                    idx_stack.pop()
        idx_stack.append(i)
    for i in range(len(idx_stack)):
        ans[idx_stack[i]] = len(prices) - idx_stack[i] - 1
    return ans