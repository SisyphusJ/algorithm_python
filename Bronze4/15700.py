a, b = map(int, input().split())

if a % 2 == 0:
    print(a * b // 2)
else:
    print((a * b // 2) + ((a * b) % 2) // 2)
