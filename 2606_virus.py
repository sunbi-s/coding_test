import sys


def dfs(graph, visited, node):
    visited[node] = True
    count = 1
    for neighbor in graph[node]:
        if not visited[neighbor]:  # 오타 수정
            count += dfs(graph, visited, neighbor)
    return count


N = int(sys.stdin.readline())
n_link = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)  # 변수명 수정

for _ in range(n_link):
    start, end = map(int, sys.stdin.readline().split())  # split() 괄호 추가
    graph[start].append(end)
    graph[end].append(start)

count = dfs(graph, visited, 1) - 1  # 문제는 감염된 컴퓨터 수니까, 자기 자신은 빼야 함
print(count)
