a, i = map(int, input().split())

if (a * (i - 1) + 1) < (a * i):
    print(a * (i - 1) + 1)
else:
    print(a * i)
