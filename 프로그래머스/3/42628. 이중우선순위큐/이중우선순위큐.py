import heapq

def solution(operations):
    ans = [0, 0]
    min_q = []
    max_q = []
    visited = []
    idx = 0

    for operation in operations:
        opr = operation[0]
        num = int(operation[2:])

        if opr == "I":
            heapq.heappush(min_q, (num, idx))
            heapq.heappush(max_q, (-num, idx))

            visited.append(False)
            idx += 1

        else:
            if num == 1:
                # 이미 삭제된 데이터 제거
                while max_q and visited[max_q[0][1]]:
                    heapq.heappop(max_q)

                if max_q:
                    _, index = heapq.heappop(max_q)
                    visited[index] = True

            else:
                # 이미 삭제된 데이터 제거
                while min_q and visited[min_q[0][1]]:
                    heapq.heappop(min_q)

                if min_q:
                    _, index = heapq.heappop(min_q)
                    visited[index] = True

    # 마지막에도 삭제된 데이터 제거
    while max_q and visited[max_q[0][1]]:
        heapq.heappop(max_q)

    while min_q and visited[min_q[0][1]]:
        heapq.heappop(min_q)

    if not max_q:
        return [0, 0]

    return [-max_q[0][0], min_q[0][0]]