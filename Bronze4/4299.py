a, b = map(int, input().split())
if a == 0 and b == 0:
    print(0, 0)
else:
    if a > b:
        if (a - b) % 2 == 0:
            print((a + b) // 2, a - ((a + b) // 2))
        else:
            print(-1)
    else:
        print(-1)
