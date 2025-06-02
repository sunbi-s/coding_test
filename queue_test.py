from collections import deque
import sys

input = sys.stdin.readline
q = deque()

def pop(): print(q.popleft() if q else -1)
def size(): print(len(q))
def empty(): print(0 if q else 1)
def front(): print(q[0] if q else -1)
def back(): print(q[-1] if q else -1)

cmd_table = {
    "pop": pop,
    "size": size,
    "empty": empty,
    "front": front,
    "back": back
}

N = int(input())
for _ in range(N):
    parts = input().strip().split()
    if parts[0] == "push":
        q.append(int(parts[1]))
    else:
        cmd_table[parts[0]]()
