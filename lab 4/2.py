list1 = ["Hello ", "take "]

list2 = ["Dear", "Sir"]

# lengthy method
l3 = []
for i in list1:
    for j in list2:
        l3.append(i + j)
        

#list comprehension
l4 = [x + y for x in list1 for y in list2]

print(l3)
print(l4)
