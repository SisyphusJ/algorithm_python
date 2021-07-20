a, b = map(int, input().split())
n = min(a, b)
m = max(a, b)

if 3 * n <= m:
    print("{:4f}".format(n))
elif 1.5 * n < m < 3 * n:
    print("{:4f}".format(m / 3))
else:
    print("{:4f}".format(n / 2))
