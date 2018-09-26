alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# create example 2d array for sales
import random
sales = []
salescount = []
for i in range(26):
    salescount.append(int(i+1)) # create 25 example sales values
for i in range(26):
    salecount = random.choice(salescount)
    salescount.remove(salecount)
    sales.append([alphabet[i],salecount])

# actual program
# sort items by sale value
swapped = True
while swapped:
    swapped = False
    for i in range(len(sales)-1):
        if sales[i][1] > sales[i+1][1]:
            sales[i],sales[i+1] = sales[i+1],sales[i]
            swapped = True
for i in range(len(sales)-1,-1,-1):
    print('Item ' + sales[i][0] + ', value = ' + str(sales[i][1]))
