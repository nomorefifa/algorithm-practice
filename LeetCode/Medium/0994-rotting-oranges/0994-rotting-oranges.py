from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = [-1, 1, 0, 0]
        col = [0, 0, -1, 1]
        
        cnt_one = 0
        q = deque()
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    cnt_one += 1
        
        ans = 0

        while q and cnt_one > 0:
            size = len(q)
            for i in range(size):
                cur_row, cur_col = q.popleft()
                for j in range(4):
                    next_row = cur_row + row[j]
                    next_col = cur_col + col[j]
                    if 0 <= next_row < m and 0 <= next_col < n:
                        if grid[next_row][next_col] == 1:
                            grid[next_row][next_col] = 2
                            cnt_one -= 1
                            q.append((next_row, next_col))
            ans += 1
        
        if cnt_one == 0:
            return ans
        else:
            return -1