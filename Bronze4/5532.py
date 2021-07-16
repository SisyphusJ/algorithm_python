import math

le = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

ko = math.ceil(a / c)
ma = math.ceil(b / d)

print(le - max(ko, ma))
