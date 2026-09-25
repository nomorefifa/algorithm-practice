dir_row = [-1, 1, 0, 0]
dir_col = [0, 0, -1, 1]
dir_dict = {"N":0, "S":1, "W":2, "E":3}
def solution(park, routes):
    cur_row = 0
    cur_col = 0
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                cur_row = i
                cur_col = j

    for i in range(len(routes)):
        dir = routes[i][0]
        size = int(routes[i][2])
        next_row = cur_row
        next_col = cur_col
        tmp_row = next_row
        tmp_col = next_col
        flag = True
        for j in range(size):
            tmp_row += dir_row[dir_dict[dir]]
            tmp_col += dir_col[dir_dict[dir]]
            if 0 <= tmp_row < len(park) and 0 <= tmp_col < len(park[0]):
                if park[tmp_row][tmp_col] == "X":
                    flag = False
                    break
            else:
                flag = False
                break
        if flag:
            cur_row = tmp_row
            cur_col = tmp_col
    return [cur_row, cur_col]