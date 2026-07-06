s=1
for i in range(5):
    for j in range(5, 0, -1):
        if j == s:
            print("*", end=" ")
        else:
            print(j, end=" ")
    s=s+1
    print()