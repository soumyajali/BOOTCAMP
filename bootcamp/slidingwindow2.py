count = 0
k = 3
a = [3, 9, 8, 3, 4, 2, 6]

for i in range(k - 1, len(a)):
    if a[i] % 2 == 0:
        count = count + 1

print(count)