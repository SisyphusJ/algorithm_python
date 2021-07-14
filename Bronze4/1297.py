d, h, w = map(int, input().split())
x = d / pow((pow(h, 2) + pow(w, 2)), 0.5)
print(int(x * h), int(x * w))
