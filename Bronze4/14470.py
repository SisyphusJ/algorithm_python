a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
time = 0
if a < 0:
    time = abs(a) * c + d + b * e
elif a > 0:
    time = (b - a) * e
print(time)
