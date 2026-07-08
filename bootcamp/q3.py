arr = [2, 3, 4, 4, 5, 6, 9, 11, 12, 15, 17, 18]

c = 0
i = 0

while i < len(arr)-1:
    if arr[i] + 1 == arr[i+1]:
        if i == 0 or arr[i] - 1 != arr[i-1]:
            c += 1
    i += 1

print(c)