name = input("Enter your name: ")
cnic = int(input("enter you cnic: "))
age = int(input("Enter your age: "))
salary = int(input("Enter your salary: "))

try: 

    with open(r"c:\\Users\\k230061\Desktop\\1.py\\4.txt", "w") as f:
        f.write(f"name: {name}\ncninc: {cnic}\nage: {age}\nsalary: {salary}\n")

    contact = int(input("Enter your contact number: "))

    with open(r"c:\\Users\\k230061\Desktop\\1.py\\4.txt", "a") as f:
        f.write(f"contact: {contact}")

except Exception as e:
    print("Error : " + str(e))