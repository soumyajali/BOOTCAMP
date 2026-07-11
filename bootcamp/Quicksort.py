arr = [9, 1, 8, 7, 5, 2, 6]

left = []
right = []

for num in arr:
    if num % 2 == 0:
        right.append(num)
    else:
        left.append(num)

print("left =", left)
print("right =", right)