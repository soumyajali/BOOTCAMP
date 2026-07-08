arr = [1, 5, 2, 3, 8, 4, 7]

c = 0
i = 0

while i < len(arr)-2:
    if arr[i+1] > arr[i] and arr[i+1] > arr[i+2]:
        c += 1
        i += 3       # skip next 2 elements (no overlap)
    else:
        i += 1

print(c)