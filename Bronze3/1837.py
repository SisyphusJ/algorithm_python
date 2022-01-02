p, k = map(int, input().split())
p1 = 0
p2 = 0
bool = 1

for i in range(2, k):
    if p % i == 0:
        p1 = i
        p2 = p // p1
        bool = 0
        break

if bool == 1:
    print("GOOD")
elif bool == 0:
    print("BAD", min(p1, p2))



