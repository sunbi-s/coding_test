def solution(friends, gifts):
    n = len(friends)
    name_to_index = {name: i for i, name in enumerate(friends)}

    # [giver][receiver] 형태의 2차원 배열
    gift_matrix = [[0] * n for _ in range(n)]

    # 선물 지수 계산용
    gift_score = [0] * n

    for record in gifts:
        giver_name, receiver_name = record.split()
        giver = name_to_index[giver_name]
        receiver = name_to_index[receiver_name]

        gift_matrix[giver][receiver] += 1
        gift_score[giver] += 1
        gift_score[receiver] -= 1

    max_future_gifts = 0

    for i in range(n):
        future_gifts = 0
        for j in range(n):
            if i == j:
                continue

            if gift_matrix[i][j] > gift_matrix[j][i]:
                future_gifts += 1
            elif gift_matrix[i][j] == gift_matrix[j][i] and gift_score[i] > gift_score[j]:
                future_gifts += 1

        max_future_gifts = max(max_future_gifts, future_gifts)

    return max_future_gifts
