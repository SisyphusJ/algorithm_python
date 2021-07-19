li = [0 for i in range(5)]
for i in range(5):
    li[i - 1] = int(input())
    if li[i - 1] < 40:
        li[i - 1] = 40
print(sum(li) // 5)
