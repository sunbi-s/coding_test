import sys

N, M = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]
coins.sort(reverse=True)  # 큰 금액부터 사용

total_count = 0

for coin in coins:
    if M == 0:
        break
    count = M // coin
    M -= count * coin
    total_count += count

print(total_count)
