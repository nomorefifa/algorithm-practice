n = int(input())
ans = []
count = 0

def is_beautiful():
    i = 0
    while i < n:
        current_num = ans[i]
        
        # 1. 묶음을 만들기 전에 범위를 초과하는지 검사 (ex. 마지막에 2가 하나만 남은 경우)
        if i + current_num > n:
            return False
            
        # 2. current_num의 개수만큼 실제로 연속해서 똑같은 숫자가 나오는지 검사
        for j in range(i, i + current_num):
            if ans[j] != current_num:
                return False
                
        # 3. 묶음 길이만큼 인덱스를 통째로 점프
        i += current_num
        
    return True

def recur(cnt):
    global count
    
    # N자리의 숫자가 완성되었을 때 (종료 조건)
    if cnt == n:
        if is_beautiful():
            count += 1
        return
        
    # 1부터 4까지의 숫자 중 하나를 선택 (문제에서 숫자는 1~4로 이루어져 있다고 제한함)
    for i in range(1, 5):
        ans.append(i)
        recur(cnt + 1)
        ans.pop() # 백트래킹

recur(0)
print(count)