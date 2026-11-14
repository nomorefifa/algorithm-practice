T = 10

for test_case in range(1, T + 1):
    n = int(input())
    nlist = list(map(int, input().split()))

    order_n = int(input())
    order = input().split()
    order_idx = 0

    for i in range(order_n):
        x = int(order[order_idx + 1])
        y = int(order[order_idx + 2])

        num_list = []
        for j in range(order_idx + 3, order_idx + 3 + y):
            num_list.append(int(order[j]))

        # 다음 명령어의 I로 이동
        order_idx += 3 + y

        # 앞의 x개를 제외한 나머지를 뒤에서부터 보관
        tmp = []
        pop_num = len(nlist) - x

        for j in range(pop_num):
            tmp.append(nlist.pop())

        # 새 숫자를 순서대로 추가
        for j in range(y):
            nlist.append(num_list[j])

        # 꺼낸 숫자를 원래 순서대로 다시 추가
        for j in range(pop_num - 1, -1, -1):
            nlist.append(tmp[j])

    print(f"#{test_case}", *nlist[:10])