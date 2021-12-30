number = int(input())
li = []
result = ''

for i in str(number):
    li.append(i)


def converter(digit):
    if digit == "0":
        return "000"
    elif digit == "1":
        return "001"
    elif digit == "2":
        return "010"
    elif digit == "3":
        return "011"
    elif digit == "4":
        return "100"
    elif digit == "5":
        return "101"
    elif digit == "6":
        return "110"
    elif digit == "7":
        return "111"


for i in range(len(li)):
    result = result + converter(li[i])

if result[0] == "0":
    if result[1] == "0":
        result = result[2:]
    else:
        result = result[1:]

print(result)
