a, b = map(int, input().split())
min = min(a, b)
max = max(a, b)
print(max * (max + 1) // 2 - (min - 1) * min // 2)

