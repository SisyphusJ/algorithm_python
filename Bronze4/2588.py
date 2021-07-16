a = int(input())
b = int(input())

a1 = b % 10
a2 = (b % 100 - a1) // 10
a3 = b // 100

print(a1 * a, a2 * a, a3 * a, a * b)
