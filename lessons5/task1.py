import random
mylist = []
while len(mylist)<10:
    mylist.append(random.randint(1,100))
max_val = mylist[0]
i = 0
while i < len(mylist):
    if max_val < mylist[i]:
        max_val = mylist[i]
    i += 1
print(f"В листе {mylist}\nмаксимальное число {max_val}")
