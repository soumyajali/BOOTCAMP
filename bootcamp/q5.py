arr = [5, 7, 8, 4, 9, 2, 3]

first_even = -1
last_odd = -1

i = 0
while i < len(arr):
    if arr[i] % 2 == 0:
        first_even = i
        break
    i += 1

i = len(arr) - 1
while i >= 0:
    if arr[i] % 2 != 0:
        last_odd = i
        break
    i -= 1

if first_even != -1 and last_odd != -1:
    temp = arr[first_even]
    arr[first_even] = arr[last_odd]
    arr[last_odd] = temp

print(arr)