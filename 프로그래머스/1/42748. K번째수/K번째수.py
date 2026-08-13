def solution(array, commands):
    ans = []
    for i in range(len(commands)):
        tmp_list = sorted(array[commands[i][0] - 1: commands[i][1]])
        ans.append(tmp_list[commands[i][2] - 1])
    return ans