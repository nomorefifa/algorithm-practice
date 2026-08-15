def solution(numbers):
    ans = ""
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    numbers = sorted(numbers, key = lambda x: x * 3)
    for i in range(len(numbers) - 1, -1, -1):
        ans += numbers[i]
    return "0" if ans[0] == "0" else ans