from sys import stdin


def inp():
    n = int(stdin.readline())
    li = [int(stdin.readline()) for i in range(n)]
    return li


def check(result):
    if result < 0:
        print("-")
    elif result == 0:
        print("0")
    else:
        print("+")


li1 = inp()
li2 = inp()
li3 = inp()
check(sum(li1))
check(sum(li2))
check(sum(li3))
