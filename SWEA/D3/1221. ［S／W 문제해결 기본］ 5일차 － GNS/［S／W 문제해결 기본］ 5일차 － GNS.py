T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
ndict = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
rndict = {0:"ZRO", 1:"ONE", 2:"TWO", 3:"THR", 4:"FOR", 5:"FIV", 6:"SIX", 7:"SVN", 8:"EGT", 9:"NIN"}
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    f, n = input().split()
    n = int(n)
    nlist = list(input().split())
    for i in range(n):
        nlist[i] = ndict[nlist[i]]
    nlist.sort()
    for i in range(n):
        nlist[i] = rndict[nlist[i]]
    print(f"#{test_case}")
    print(" ".join(nlist))
    # ///////////////////////////////////////////////////////////////////////////////////
