q = ["1)What is the base damage of vandal?",
     "2)How much does sage heal?", "3)What is the price of odin?"]
a, l, z = ['40', '60', '3600'], [], 0
for i in q:
    print(i)
    v = input()
    l.append(v)
for i in range(3):
    if a[i] == l[i]:
        z = z+1
print("total points:", z)
