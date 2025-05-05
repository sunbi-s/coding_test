import math

def solution(players, m, k):
    """
    players: 각 시간대별 유저 수 (길이 24)
    m: 서버 1대당 수용 가능한 유저 수
    k: 증설 서버의 유지 시간
    """

    # 각 시간대별 추가 증설 서버 수 저장
    server_add = {hour: 0 for hour in range(24)}

    for hour in range(24):
        # 기본적으로 서버 1대는 항상 운영 중
        active_servers = 1

        # 최근 k시간 동안 증설된 서버 수 누적
        for prev_hour in range(max(0, hour - (k - 1)), hour + 1):
            active_servers += server_add[prev_hour]

        # 현재 시간대 유저 수가 서버 수용량 초과하면 서버 증설
        if players[hour] >= active_servers * m:
            need = players[hour] - (active_servers * m - 1)  # -1로 경계 포함
            server_add[hour] = math.ceil(need / m)

    # 디버깅 출력 (필요 없으면 제거 가능)
    # print(server_add)

    # 총 증설 서버 수 반환
    return sum(server_add.values())