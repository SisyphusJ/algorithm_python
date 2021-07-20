d, h, m = map(int, input().split())
time = (d - 11) * 24 * 60 + (h - 11) * 60 + (m - 11)
if time < 0:
    print(-1)
else:
    print(time)
