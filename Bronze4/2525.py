a, b = map(int, input().split())
c = int(input())
if b + c >= 60:
    if (b + c) // 60 + a >= 24:
        print((b + c) // 60 + a - 24, (b + c) % 60)
    else:
        print((b + c) // 60 + a, (b + c) % 60)
else:
    print(a, b + c)
