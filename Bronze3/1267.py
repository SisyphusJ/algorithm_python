import math

n = int(input())
li = list(map(int, input().split()))
yeongsik = []
minsik = []


def cal(time):
    if time == 0 or time % 15 == 0 or time % 60 == 0:
        time = time + 1

    yeongsik.append((math.ceil(time / 30)) * 10)
    minsik.append((math.ceil(time / 60)) * 15)


for i in range(n):
    cal(li[i])

if sum(yeongsik) < sum(minsik):
    print("Y", sum(yeongsik))
elif sum(yeongsik) == sum(minsik):
    print("Y M", sum(yeongsik))
else:
    print("M", sum(minsik))
