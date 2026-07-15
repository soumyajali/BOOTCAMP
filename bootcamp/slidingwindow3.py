a = [3, 9, 8, 3, 4, 2, 1]
k = 3

count = 0

for i in range(len(a) - k + 1):
    even = 0
    for j in range(i, i + k):
        if a[j] % 2 == 0:
            even += 1
    if even > k // 2:
        count += 1

print(count)