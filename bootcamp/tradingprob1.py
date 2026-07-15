a = [3, 9, 4, 1, 7]
max_profit = 0

for i in range(len(a)):
    for j in range(i, len(a)):
        profit = a[j]-a[i]
        if profit > max_profit:
            max_profit=profit

print(max_profit)