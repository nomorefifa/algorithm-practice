
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

x1 = [i[0] for i in segments]
x2 = [i[1] for i in segments]

# 미리 오름차순으로 정렬해둡니다. (O(N log N))
sorted_x1 = sorted(x1)
sorted_x2 = sorted(x2)

ans = float('inf')

for i in range(n):
    # i번째 선분을 제거했을 때의 새로운 최솟값 찾기
    # 만약 지우려는 선분의 x1이 전체에서 가장 작은 값이라면, 두 번째로 작은 값이 새로운 최솟값이 됨
    if x1[i] == sorted_x1[0]:
        new_min = sorted_x1[1]
    else:
        new_min = sorted_x1[0]
        
    # i번째 선분을 제거했을 때의 새로운 최댓값 찾기
    # 만약 지우려는 선분의 x2가 전체에서 가장 큰 값이라면, 두 번째로 큰 값이 새로운 최댓값이 됨
    if x2[i] == sorted_x2[-1]:
        new_max = sorted_x2[-2]
    else:
        new_max = sorted_x2[-1]
        
    # 최솟값 갱신
    if new_max - new_min < ans:
        ans = new_max - new_min

print(ans)