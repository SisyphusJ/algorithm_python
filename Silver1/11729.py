def check(b):
    s = 0
    rb = "".join(reversed(b))
    for j in range(len(rb)):
        if rb[j] == "1":
            return j


n = int(input())
m = pow(2, n)
location = [1 for _ in range(n + 1)]
print(m - 1)
if n % 2 == 1:
    for i in range(1, m):
        num = int(check(str(bin(i)[2:]))) + 1

        if num % 2 == 1:
            if location[num] == 1:
                print("%d %d" % (location[num], 3))
                location[num] = 3
            else:
                print("%d %d" % (location[num], location[num] - 1))
                location[num] -= 1

        else:

            if location[num] == 3:
                print("%d %d" % (location[num], 1))
                location[num] = 1
            else:
                print("%d %d" % (location[num], location[num] + 1))
                location[num] += 1

else:
    for i in range(1, m):
        num = int(check(str(bin(i)[2:]))) + 1

        if num % 2 == 1:
            if location[num] == 3:
                print("%d %d" % (location[num], 1))
                location[num] = 1
            else:
                print("%d %d" % (location[num], location[num] + 1))
                location[num] += 1

        else:
            if location[num] == 1:
                print("%d %d" % (location[num], 3))
                location[num] = 3
            else:
                print("%d %d" % (location[num], location[num] - 1))
                location[num] -= 1
