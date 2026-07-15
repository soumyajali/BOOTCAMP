s = [3, 9, 4, 1, 10]

p = 0
mp = 0
buy = []
sell = []

mine = s[0]
maxe = s[-1]
for i in range(len(s)):
    if s[i] < mine:
        mine = s[i]
    buy.append(mine)

for i in range(len(s)-1, -1, -1):
    if s[i] > maxe:
        maxe = s[i]
    sell.append(maxe)

sell.reverse()
for i in range(len(s)):
    p = sell[i] - buy[i]
    if p > mp:
        mp = p

print("Buy :", buy)
print("Sell:", sell)
print("Maximum Profit:", mp)