import sys
sys.setrecursionlimit(10000)

T = int(sys.stdin.readline())

def dfs(x, nums, visited):
    visited[x] = True
    next_node = nums[x]
    if not visited[next_node]:
        dfs(next_node, nums, visited)

for _ in range(T):
    n = int(sys.stdin.readline())
    perm = list(map(int, sys.stdin.readline().split()))
    perm.insert(0, 0)  # 1-based index

    visited = [False] * (n + 1)
    cycle_count = 0

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, perm, visited)
            cycle_count += 1

    print(cycle_count)