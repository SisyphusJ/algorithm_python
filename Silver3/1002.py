def check(list):
    b = list[2] + list[5]
    d = ((list[0] - list[3]) ** 2 + (list[1] - list[4]) ** 2) ** (1 / 2)

    if list[2] == list[5] and d == 0:
        return -1

    if b < d:
        return 0
    elif b == d:
        return 1
    else:
        if d + min(list[2], list[5]) == max(list[2], list[5]):
            return 1
        elif d + min(list[2], list[5]) < max(list[2], list[5]):
            return 0
        else:
            return 2


n = int(input())
case = [0 for _ in range(6)]
result = [0 for _ in range(n)]

for i in range(n):
    case = [int(x) for x in input().split()]
    result[i] = check(case)

for i in range(n):
    print(result[i])
