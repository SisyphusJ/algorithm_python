a = input()
b = input()


def bi(srd):
    di = len(srd)
    s = 0
    for i in range(len(srd)):
        if srd[di - i - 1] == "1":
            s += pow(2, i)
    return s


result = bi(a) * bi(b)
print(format(result, 'b'))
