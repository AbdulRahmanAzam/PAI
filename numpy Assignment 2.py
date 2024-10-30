import numpy as np

# Question 1
arr = np.arange(1, 11)
arr_sum = arr.sum()
arr_mean = arr.mean()
arr_prod = arr.prod()
print(f"Sum: {arr_sum} \nMean: {arr_mean} \nProduct: {arr_prod}\n")

# Question 2
arr = np.random.randint(1,10, (3,3))
print(f"Matrix: {arr}")
matrix_transpose = arr.T
print(f"Matrix Transpose: {matrix_transpose}\n")

# Question 3
arr_20 = np.arange(1,21)
reshape_20 = arr_20.reshape(4, 5)

print(f"Reshaped array: {reshape_20}\n")

# Question 4
arr1 = np.random.randint(1,6)
arr2 = np.random.randint(6,11)

arr_addition = arr1 + arr2
arr_subtraction = arr1 - arr2
arr_multiplication = arr1 * arr2
arr_division = arr1 / arr2

print(f"Addition: {arr_addition}")
print(f"Subtraction: {arr_subtraction}")
print(f"Multiplication: {arr_multiplication}")
print(f"Division: {arr_division}\n")


# Question 5
arr_10 = np.arange(1, 11)
arr_10 = np.sqrt(arr_10)
print(f"Square root of array: {arr_10}")


# Question 6
matrix = np.random.randint(1, 10, (2, 2))
determinant = np.linalg.det(matrix)

inverse = np.invert(matrix)

print(f"Determinant: {determinant} \nInverse: \n{inverse}")

# Question 7
arr_50 = np.random.rand(50)
max_no = np.argmax(arr_50)
min_no = np.argmin(arr_50)
print(f"Max number: {max_no}")
print(f"Min Number: {min_no}\n")


# Question 8
coeff = np.random.rand(3,3)
const = np.random.rand(3)
solution = np.linalg.solve(coeff, const)
print(f"The solution is: {solution}\n")


# Question 9 
arr_25 = np.arange(1,26)
percentile_75 = np.percentile(arr_25, 75)
print(f"75 percentile is: {percentile_75}\n")

# Question 10
def normalize_array(arr):
    return (arr - np.mean(arr)) / np.std(arr)

arr = np.arange(1,11)
print(f"The normalized array is: {normalize_array(arr)}")
