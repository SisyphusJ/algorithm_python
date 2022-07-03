array = list(i for i in range(1, 10001))

for i in range(1, 10001):
    s = str(i)
    d = i
    for j in s:
        d += int(j)
    if d in array:
        array.remove(d)

for i in array:
    print(i)
