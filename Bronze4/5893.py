n = input()
n_len = len(n)
a = 0
for i in range(n_len):
    if n[n_len - i - 1] == "1":
        a += 2 ** i
print(format((a * 17), 'b'))
