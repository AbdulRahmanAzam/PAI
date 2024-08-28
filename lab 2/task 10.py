# def build_message(**info):
#     print(*info)

def build_message(**info):
    for i in info.values():
        print(i)


name = input("Enter your name: ")
age = input("Enter your age: ")
school = input("Enter name of your school: ")
city = input("Enter your city: ")
country = input("Enter your country: ")

build_message(name=name, age=age, school=school, city=city, country=country)

