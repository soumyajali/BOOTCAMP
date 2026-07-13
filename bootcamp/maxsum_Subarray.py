a = [1,2,3]
sum = 0
max = 0

for i in range(0,len(a)):
    sum = 0
    for j in range(1,len(a)):
        sum = sum + a[j]
        if sum > max:
            max  =  sum

print(max )