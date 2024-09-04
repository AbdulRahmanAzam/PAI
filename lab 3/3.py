l1 = list()
l2 = list()
dic = {}

n = 3
try:

    for i in range(n):
        a = int(input("Enter no for list 1: "))
        l1.append(a)


    for i in range(n):
        a = int(input("Enter no for list 2: "))
        l2.append(a)


    for i in range(n):
        dic[f"{l1[i]}"] = f"{l2[i]}"

    with open(r"c:\\Users\\k230061\Desktop\\1.py\\3.txt", "w") as f:
        f.write(f"{dic}")

    print(dic)

except Exception as e:
    print("Error : " + str(e))