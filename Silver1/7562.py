import sys
from collections import deque

x1 = [-1, -2, -2, -1, 1, 2, 2, 1]
y2 = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs(x, y, dx, dy, i):
    queue = deque()
    queue.append([x, y])
    graph[x][y] = 1

    while queue:
        x, y = queue.popleft()
        if x == dx and y == dy:
            return graph[x][y] - 1
        for j in range(8):
            if 0 <= x + x1[j] < i and 0 <= y + y2[j] < i:
                tempx = x + x1[j]
                tempy = y + y2[j]
                if graph[tempx][tempy] == 0:
                    graph[tempx][tempy] = graph[x][y] + 1
                    queue.append([tempx, tempy])


n = int(input())
ans = []
for _ in range(n):
    i = int(input())
    x, y = map(int, sys.stdin.readline().split())
    dx, dy = map(int, sys.stdin.readline().split())
    graph = [[0] * i for _ in range(i)]

    if x == dx and y == dy:
        ans.append(0)
        continue
    ans.append(bfs(x, y, dx, dy, i))

for i in range(len(ans)):
    print(ans[i])
