def solution(phone_book):
    phone_dict = {}
    ans = True
    for num in range(len(phone_book)):
        phone_dict[phone_book[num]] = 1
    for i in range(len(phone_book)):
        tmp_num = ""
        phone_dict[phone_book[i]] = 0
        for j in range(len(phone_book[i])):
            tmp_num += phone_book[i][j]
            if tmp_num in phone_dict and phone_dict[tmp_num] == 1:
                ans = False
        phone_dict[phone_book[i]] = 1
    return ans