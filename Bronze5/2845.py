l, p = map(int, input().split(" "))
pop = map(int, input().split(" "))
result = []
for i in pop:
    result.append(i - (l * p))
for n in range(len(result)):
    print(result[n], end=" ")
