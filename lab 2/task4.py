def employee(name,salary = 10000):
    tax = salary * (2 / 100)

    salary = salary - tax

    return salary,name

name = str(input('Enter the name: '))
salary = int(input('Enter the salary: '))

print(employee(name,salary))
print(employee(name))
