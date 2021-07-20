a, b = map(int, input().split())
n, m = map(int, input().split())

x = a + m
y = n + b

print(min(x, y))
