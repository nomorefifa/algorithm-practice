n, q = map(int, input().split())
points = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# 1. 정렬 (매우 잘하셨습니다!)
points.sort()

for i in range(q):
    s_target = queries[i][0] # 구간의 시작 값
    e_target = queries[i][1] # 구간의 끝 값
    
    # ----------------------------------------------------
    # [Lower Bound] s_target '이상'인 첫 번째 위치 찾기
    # ----------------------------------------------------
    s_idx = 0
    e_idx = n  # n - 1이 아니라 n으로 해야 배열 끝까지 탐색 가능합니다.
    
    while s_idx < e_idx:
        mid = (s_idx + e_idx) // 2
        # 중간값이 타겟보다 작으면 무조건 오른쪽에 정답이 있음
        if points[mid] < s_target:
            s_idx = mid + 1
        # 중간값이 타겟보다 크거나 같으면, 왼쪽을 더 탐색해봄
        else:
            e_idx = mid
            
    start = s_idx # s_target 이상인 첫 번째 인덱스
    
    # ----------------------------------------------------
    # [Upper Bound] e_target '초과'인 첫 번째 위치 찾기
    # ----------------------------------------------------
    s_idx = 0
    e_idx = n  # 마찬가지로 n으로 설정
    
    while s_idx < e_idx:
        mid = (s_idx + e_idx) // 2
        # 중간값이 e_target보다 작거나 같으면 무조건 오른쪽에 정답이 있음
        if points[mid] <= e_target:
            s_idx = mid + 1
        # 중간값이 e_target보다 크면, 왼쪽을 더 탐색해봄
        else:
            e_idx = mid
            
    end = s_idx # e_target 초과인 첫 번째 인덱스

    # ----------------------------------------------------
    # [결과 출력] 
    # 끝 인덱스에서 시작 인덱스를 빼주기만 하면 점의 개수가 나옵니다. (+1 필요 없음)
    # 구간에 점이 없으면 자연스럽게 0이 출력됩니다.
    # ----------------------------------------------------
    print(end - start)