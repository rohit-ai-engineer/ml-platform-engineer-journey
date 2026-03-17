import numpy as np
import time

py_list = [1, 2, 3, 4, 5]
np_array = np.array([1, 2, 3, 4, 5])

print(type(py_list))
print(type(np_array))
print(np_array)

py_list = list(range(1000000))
np_array = np.array(range(1000000))

# Python list
start = time.time()
doubled_list = [x * 2 for x in py_list]
print(f"List time: {time.time() - start:.4f} seconds")

# NumPy array
start = time.time()
doubled_array = np_array * 2
print(f"NumPy time: {time.time() - start:.4f} seconds")


print(np.zeros(5))
print(np.ones(5))
print(np.arange(0, 10, 2))
print(np.linspace(0, 1, 5))


arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[-1])
print(arr[1:4])
print(arr[::2])

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matrix.shape)
print(matrix[0])
print(matrix[1][2])
print(matrix[1, 2])


a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print(a + b)
print(a * b)
print(a ** 2)
print(np.sqrt(a))


arr = np.array([1, 2, 3, 4, 5])

print(arr + 10)
print(arr * 3)

data = np.array([23, 45, 12, 67, 34, 89, 56, 78, 43, 21])

print(np.mean(data))
print(np.median(data))
print(np.std(data))
print(np.min(data))
print(np.max(data))
print(np.percentile(data, 75))

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

# print(A + B)
# print(A * B)
print(np.dot(A, B))