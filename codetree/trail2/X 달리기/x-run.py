x = int(input())

time = 0
dist = 0
v = 0 # 처음 시작하기 직전의 속도

# 도착지에 도달할 때까지 1초씩 시뮬레이션
while dist < x:
    # 1. 다음 속도 후보 (가장 빠른 +1부터 유지, -1 순서로 탐색)
    for v_next in (v + 1, v, v - 1):
        if v_next <= 0:
            continue
            
        # 2. v_next 속도를 냈을 때, 무사히 1m/s까지 감속하기 위해 필요한 최소 거리 계산
        # 1부터 v_next까지의 합 = v_next * (v_next + 1) / 2
        min_required_dist = v_next * (v_next + 1) // 2
        
        # 3. 남은 거리가 최소 안전거리보다 크거나 같다면 이 속도를 채택
        if dist + min_required_dist <= x:
            v = v_next
            dist += v
            time += 1
            break # 속도를 정했으므로 다음 초(시간)로 넘어감

print(time)