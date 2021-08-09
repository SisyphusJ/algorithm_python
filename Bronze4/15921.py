s = int(input())
if s == 0:
    print("divide by zero")
else:
    li = list(map(int, input().split()))
    ex = 0
    a = sum(li) / s
    print("{:.2f}".format(a / a))
