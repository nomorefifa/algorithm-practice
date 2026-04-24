class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        alp = []
        idx = []
        slist = [i for i in s]
        for i in range(len(s)):
            if slist[i] in vowels:
                alp.append(slist[i])
                idx.append(i)
        cnt_idx = 0
        for i in range(len(alp) - 1, -1, -1):
            slist[idx[cnt_idx]] = alp[i]
            cnt_idx += 1
        return ''.join(slist)