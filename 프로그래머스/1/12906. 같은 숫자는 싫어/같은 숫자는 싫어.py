def solution(arr):
    s = [arr[0]]
    for i in range(1, len(arr)):
        if s[-1] != arr[i]:
            s.append(arr[i])
    return s