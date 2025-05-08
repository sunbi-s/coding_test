# 물건 가치의 최대합 구하기
# 1번만 물건 사용을 위해서 거꾸로 순회

import sys
N, K = map(int, sys.stdin.readline().split())

bag = [0] * (K + 1)

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    for i in range(K, W - 1, -1):  # 거꾸로 순회 (중복 방지)
        bag[i] = max(bag[i], bag[i - W] + V)

# 결과에서 최댓값 구하기
answer = max(bag)
print(answer)