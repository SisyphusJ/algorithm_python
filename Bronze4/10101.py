li = [0 for _ in range(3)]
for i in range(3):
    li[i] = int(input())
li.sort()
if sum(li) != 180:
    print("Error")
else:
    if li[0] == li[1] == li[2]:
        print("Equilateral")
    elif li[0] == li[1] or li[1] == li[2]:
        print("Isosceles")
    elif li[0] != li[1] != li[2]:
        print("Scalene")
