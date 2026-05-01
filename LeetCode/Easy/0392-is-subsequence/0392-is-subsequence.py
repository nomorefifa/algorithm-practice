class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_point = 0
        for i in range(len(t)):
            if s_point == len(s):
                break
            if s[s_point] == t[i]:
                s_point += 1
        if s_point == len(s):
            return True
        else:
            return False