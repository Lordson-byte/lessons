i, list1 = 0, []
while i <= 100:
    i += 1
    list1.append(i)
i, list2 = 0, []
while i < len(list1):
    if list1[i]%7==0 and list1[i]%5!=0:
        list2.append(list1[i])
    i+=1
print(list2)