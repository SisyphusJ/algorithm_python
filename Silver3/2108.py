import sys
from collections import Counter


def average(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]

    return round(sum / len(array))


def center(array):
    array.sort()
    c = len(array) // 2
    return array[c]


def mode(array):
    cnt = Counter(array)
    m = cnt.most_common(2)

    if len(m) == 1:
        return m[0][0]

    if m[0][1] == m[1][1]:
        return m[1][0]
    else:
        return m[0][0]


def extent(array):
    return max(array) - min(array)


n = int(input())
li = []
for i in range(n):
    li.append(int(sys.stdin.readline()))

print(average(li))
print(center(li))
print(mode(li))
print(extent(li))
