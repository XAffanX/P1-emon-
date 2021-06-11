x = []
y = ['40', '60', '3600']
z = 0
print("1)What is the base damage of vandal?\n2)How much does sage heal?\n3)What is the price of odin?")
for i in range(0, 3):
    a = input(f'{i+1})')
    x.append(a)
for i in range(3):
    if x[i] == y[i]:
        z = z+1
print('Total Points:', z)
