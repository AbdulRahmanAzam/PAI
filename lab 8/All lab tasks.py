import numpy as np

# Question 2
arr = np.arange(1, 10).reshape(3 ,3)
for element in arr:
    print(element)
print("\n")


# Question 3
arr = np.arange(0, 18, 2).reshape(3,3)
# OR
shape = (3,3)
arr = np.arange(0, np.prod(shape) * 2, 2).reshape(shape)
print(arr)

identity = np.eye(3)

arr = arr * 4
# arr = arr * identity
arr = np.dot(arr, identity)
print(f"The answer is: \n{arr}\n")

# Question 4
student_data = np.array([
    ('Johm', 180, 12),
    ('farri', 155, 11),
    ('kiakehne', 160, 11),
    ('zabardast', 170, 12)
], dtype=[('name', 'U10'), ('height', 'i4'), ('class', 'i4')])

sorted_students = np.sort(student_data, order=['class', 'height'])
print("\nSorted student data by class and height:\n", sorted_students)


# Question 5
random_matrix = np.random.choice([2,5,9,10], size=(4,4))
identity = np.eye(4)
multiplied_matrix = np.dot(random_matrix, identity)
odd_matrix = np.arange(1, np.prod((4,4))*2, 2).reshape(4,4)
solution = multiplied_matrix + odd_matrix

print(f"{solution}\n")

# Question 6
matrix1 = np.random.randint(1, np.prod((5,3)), (5,3))
matrix2 = np.random.randint(1, np.prod((3,2)), (3,2))
print(matrix1)
print(f"{matrix2}\n")

multiplied = np.dot(matrix1, matrix2)
print(multiplied)

# Question 7
arr = np.random.rand(1000)
average = np.average(arr)
variance = np.var(arr)
std = np.std(arr)

with open("text.txt", 'w') as f:
    f.write(f"Average: {average}\nVariance: {variance}\nStandard deviation{std}")
