a, b, c = map(int, input().split())
result = 0
if b >= c:
    result = -1
else:
    result = a / (c - b) + 1

print(int(result))
