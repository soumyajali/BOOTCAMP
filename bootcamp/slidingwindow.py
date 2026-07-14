a = [7, 2, 3, 9, 5, 1, 2, 4, 3]

k = 5
sum = 0
m = 0
c = 0

for i in range(len(a)):
    if i < k:
        sum = sum + a[i]
    else:
        sum = sum + a[i] - a[i - k]

    if sum > m:
        m = sum
        c = c + 1

print(m)