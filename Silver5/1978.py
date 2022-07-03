def prime(arr):
    count = 0
    for i in arr:
        check = True
        if i == 1:
            check = False

        for j in range(2, i):
            if i % j == 0:
                check = False
                break

        if check:
            count += 1

    return count


n = int(input())
array = list(map(int, input().split()))
print(prime(array))
