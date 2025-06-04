import sys
N = int(sys.stdin.readline())

timelines = []
for _ in range(N):
    timelines.append(list(map(int, sys.stdin.readline().split())))

# 끝나는 시간, 시작 시간 순으로 정렬
timelines = sorted(timelines, key=lambda x : (x[1], x[0]))

count = 0
last_end = 0

for start, end in timelines:
    if start >= last_end:
        last_end = end
        count += 1

print(count)
