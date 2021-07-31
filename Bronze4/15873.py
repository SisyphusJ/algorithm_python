n = int(input())

if n % 10 == 0:
    a = n // 100
    b = n % 100
else:
    a = n // 10
    b = n % 10

print(a + b)
