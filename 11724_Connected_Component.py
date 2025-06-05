import sys
#재귀 깊이 조정정
sys.setrecursionlimit(10**6)

def dfs(graph, visited, node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)
            
# 정점 수 N, 간선 수 M
N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [False for _ in range(N+1)]  # 올바른 visited 초기화
component_count = 0

for i in range(1, N+1):  # 변수명 수정
    if not visited[i]:
        dfs(graph, visited, i)
        component_count += 1

print(component_count)
