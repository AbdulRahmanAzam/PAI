dic = {'Rahman' : [98,67,70,50], 'basit':[90,97,93,77]}

dic['Rahman'].append(66)

print(dic)

for i in dic:
    count = 0
    sum = 0
    for grade in dic[i]:
        count += 1
        sum += grade
    print(f"{i} got average grade of {sum/count}")

dic.update({'hehe':list()})

dic.pop('hehe')

print(dic)