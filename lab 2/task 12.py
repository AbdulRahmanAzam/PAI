l1 = list()
l2 = list()
dic = {}

n = 3

for i in range(n):
    a = int(input("Enter no for list 1: "))
    l1.append(a)


for i in range(n):
    a = int(input("Enter no for list 2: "))
    l2.append(a)


for i in range(n):
    dic[f"{l1[i]}"] = f"{l2[i]}"

print(dic)
