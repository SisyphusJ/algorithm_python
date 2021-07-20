d = int(input())
car = list(map(int, input().split()))
count = 0
for i in range(5):
    if car[i] == d:
        count += 1
print(count)
