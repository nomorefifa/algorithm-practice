def solution(brown, yellow):
    num = brown + yellow
    candidate = []
    for i in range(1, num + 1):
        if num % i == 0:
            if i >= num // i:
                candidate.append((i, num//i))
            else:
                candidate.append((num//i, i))
    for i in range(len(candidate)):
        if (candidate[i][0] - 1 + (candidate[i][1] - 1)) * 2 == brown:
            return [candidate[i][0], candidate[i][1]]