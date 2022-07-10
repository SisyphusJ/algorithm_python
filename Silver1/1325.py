import sys

m, n = input().split()
m = int(m)
n = int(n)

graph = [[0]]
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

print(graph)
