import sys
from collections import deque


def BFS(graph, root):
    count = 1
    visit = [False for _ in range(n + 1)]
    queue = deque([root])
    visit[root] = True

    while queue:
        c = queue.popleft()
        for i in graph[c]:
            if not visit[i]:
                visit[i] = True
                count += 1
                queue.append(i)

    return count


n, m = (map(int, (sys.stdin.readline().split())))
graph = [[] for _ in range(n + 1)]
max_Count = 1
result = []

for _ in range(m):
    a, b = (map(int, (sys.stdin.readline().split())))
    graph[b].append(a)

for i in range(1, n + 1):
    cnt = BFS(graph, i)
    if cnt > max_Count:
        max_Count = cnt
        result.clear()
        result.append(i)
    elif cnt == max_Count:
        result.append(i)

print(*result)
