from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
dq = deque(map(int, input().split()))
stack = []
expected = 1

while dq or stack:
    # main에서 확인
    if dq and dq[0] == expected:
        dq.popleft()
        expected += 1
    # side에서 확인
    elif stack and stack[-1] == expected:
        stack.pop()
        expected += 1
    # main에서 side로 보냄
    elif dq:
        stack.append(dq.popleft())
    # 더이상 main에서 side로 보낼 수 없는데 사람을 불러야하는경우
    else:
        print('Sad')
        break
else:
    print('Nice')
