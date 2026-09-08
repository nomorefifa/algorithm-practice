def solution(tickets):
    ap = {}

    for start, end in tickets:
        if start in ap:
            ap[start].append([end, False])
        else:
            ap[start] = [[end, False]]

    # 알파벳 순서
    for key in ap:
        ap[key].sort(key=lambda x: x[0])

    ans = ["ICN"]

    def dfs(node):
        # 모든 티켓 사용 완료
        if len(ans) == len(tickets) + 1:
            return True

        for next_node in ap.get(node, []):
            if not next_node[1]:

                # 선택
                next_node[1] = True
                ans.append(next_node[0])

                if dfs(next_node[0]):
                    return True

                # 선택 취소 → 백트래킹
                ans.pop()
                next_node[1] = False

        return False

    dfs("ICN")

    return ans