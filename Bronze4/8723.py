li = list(map(int, input().split()))
li.sort()
if li[0] == li[1] and li[1] == li[2]:
    print(2)
elif pow(li[0], 2) + pow(li[1], 2) == pow(li[2], 2):
    print(1)
else:
    print(0)
