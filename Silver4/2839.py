n = int(input())
if n % 5 == 0:
    print(n // 5)
else:
    temp = n
    count = 0
    check = True
    while temp >= 0:
        temp -= 3
        count += 1
        if temp % 5 == 0:
            print(count + temp // 5)
            check = False
            break

    if check:
        print(-1)
