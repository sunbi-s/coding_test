import sys

# 입력
N = int(sys.stdin.readline())

# 3개의 기둥 (스택 구조)
A = list(range(N, 0, -1))  # 1번 기둥
B = []  # 2번 기둥
C = []  # 3번 기둥
pegs = {1: A, 2: B, 3: C}

# 이동 경로 저장
moves = []


def hanoi(n, src, dst, aux):
    if n == 1:
        # 실제 이동
        pegs[dst].append(pegs[src].pop())
        moves.append((src, dst))
    else:
        hanoi(n - 1, src, aux, dst)
        pegs[dst].append(pegs[src].pop())
        moves.append((src, dst))
        hanoi(n - 1, aux, dst, src)


# 실행
hanoi(N, 1, 3, 2)

# 출력
print(len(moves))  # 총 이동 횟수
for move in moves:
    print(f"{move[0]} {move[1]}")
