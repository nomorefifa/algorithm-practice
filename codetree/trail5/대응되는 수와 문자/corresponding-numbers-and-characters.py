n, m = map(int, input().split())

# Note: Using 1-based indexing for words as per C++ code
words = [""] + [input() for _ in range(n)]
queries = [input() for _ in range(m)]

# Please write your code here.

alp_dict = {}
for i in range(1, n + 1):
    alp_dict[words[i]] = i

for q in queries:
    if q.isdigit():
        idx = int(q)
        print(words[idx])
    else:
        print(alp_dict[q])