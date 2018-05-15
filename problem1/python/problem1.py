list = []
limit = 1000
total = 0
for x in range(limit):
    if(x%3==0) or (x%5==0):
        list.append(x)

for int in list:
    total+=int

print(total)
