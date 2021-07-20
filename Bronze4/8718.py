x, k = map(int, input().split())

caseM = 3500 * k
caseL = 7000 * k
caseH = 1750 * k
li = [caseL, caseM, caseH]
for i in range(len(li)):
    if li[i] > 1000 * x:
        li[i] = 0
print(max(li))
