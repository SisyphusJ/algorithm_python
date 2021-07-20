k, w, m = map(int, input().split())
time = (w - k) // m
if time < 0:
    print(0)
elif time * m + k < w:
    print(time + 1)
elif time * m + k <= w:
    print(time)
