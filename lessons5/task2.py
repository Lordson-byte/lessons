import random
list1, list2 = [], []
while len(list1) < 10:
    list1.append(random.randint(1, 10))
while len(list2) < 10:
    list2.append(random.randint(1, 10))
i = 0
list3 = []
while i < len(list1):
    if (list1[i] in list2) and (list1[i] not in list3):
         list3.append(list1[i])
    i+=1

print(list1, list2, list3)