def solution(s, skip, index):
    ans = ''
    skip = set(skip)
    for i in range(len(s)):
        cur_alp = ord(s[i]) - ord('a')
        cnt = 0
        while cnt < index:
            next_alp = chr((cur_alp + 1) % 26 + ord('a'))
            if next_alp not in skip:
                cnt += 1
            cur_alp = ord(next_alp) - ord('a')
        ans += chr(cur_alp + ord('a'))
    return ans