a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

y = 0
x = a * p
if p <= c:
    y = b
else:
    y = (p - c) * d + b
print(min(x, y))
