mL, mR, tL, tR = map(str, input().split(" "))
mCount = 0
tCount = 0


def check(shape, shape2):
    global mCount
    global tCount
    if shape == "R":
        if shape2 == "S":
            mCount += 1
        elif shape2 == "P":
            tCount += 1

    elif shape == "S":
        if shape2 == "P":
            mCount += 1
        elif shape2 == "R":
            tCount += 1

    elif shape == "P":
        if shape2 == "R":
            mCount += 1
        elif shape2 == "S":
            tCount += 1


check(mL, tL)
check(mL, tR)
check(mR, tL)
check(mR, tR)

if tCount == 4:
    print("TK")
elif mCount == 4:
    print("MS")
else:
    if mL == mR:
        if tCount == 2:
            print("TK")
        else:
            print("?")
    elif tL == tR:
        if mCount == 2:
            print("MS")
        else:
            print("?")

    else:
        print("?")
