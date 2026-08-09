def solution(clothes):
    clothes_dict = {}
    ans = 1
    for i in range(len(clothes)):
        if clothes[i][-1] in clothes_dict:
            clothes_dict[clothes[i][-1]] += 1
        else:
            clothes_dict[clothes[i][-1]] = 1
    for i in range(len(list(clothes_dict.keys()))):
        ans *= clothes_dict[list(clothes_dict.keys())[i]] + 1
    return ans - 1