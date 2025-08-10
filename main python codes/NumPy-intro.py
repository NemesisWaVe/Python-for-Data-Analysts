
import numpy as np #renaming your package as other name makes it easier to call

# --- What is NumPy? ---
# NumPy (Numerical Python) is the fundamental package for numerical computation in Python.
# It provides a powerful N-dimensional array object, and tools for working with these arrays.
# It's the foundation for many other data science libraries, including Pandas.

# --- Creating NumPy Arrays ---
# You can create a NumPy array from a Python list.
my_list = [1, 2, 3, 4, 5]
numpy_array = np.array(my_list) 

print("--- NumPy Array ---")
print(numpy_array)
print(f"Type of the array: {type(numpy_array)}")


# --- Why use NumPy arrays over Python lists? ---
# 1. They are much faster for numerical operations.
# 2. They allow for "vectorized" operations, where you can perform an operation on the entire array at once.

# For example, let's try to multiply every element by 2.
# With a list, you would need a loop:
doubled_list = [x * 2 for x in my_list]
print(f"\nDoubled list (using a loop): {doubled_list}")

# With a NumPy array, it's much simpler and faster:
doubled_numpy_array = numpy_array * 2
print(f"Doubled NumPy array (vectorized): {doubled_numpy_array}")


# --- Basic Array Operations ---
# You can perform all standard mathematical operations.
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
b = np.array([[1,2],[3,4]]) # Create a 2d array like this you can create array with different dimensions
print(b)
print(f"2D array size: {b.shape}") #prints size of array

# Addition
print(f"\nArray A + Array B = {array_a + array_b}")

# Multiplication
print(f"Array A * Array B = {array_a * array_b}")

# --- Useful NumPy Functions ---
# NumPy has many useful functions for creating arrays or analyzing them.

# Create an array of all zeros
zeros_array = np.zeros(5)
print(f"\nAn array of zeros: {zeros_array}")

# Create an array of all ones
ones_array = np.ones((1,2))
print(f"\nAn array of ones: {ones_array}")

# Create a constant array
constant_array= np.full((2,2), 6)
print(f"\nAn array of constants:\n {constant_array}")

# Create a 2x2 identity matrix
identity_matrix= np.eye(2) 
print(f"\nAn identity matrix:\n {identity_matrix}")

# Create an array within a range
range_array = np.arange(0, 10, 2) # Start, Stop (exclusive), Step
print(f"\nAn array from a range: {range_array}")

#The linspace function is similar, but we can specify the number of values instead of
#the step size, and it will create a sequence of evenly spaced values.
linespace_array = np.arange(10,50,5) # Create an array of values starting at 10 in increments of 5
print(f"\nAn array from a range: {linespace_array}")

# Create an array filled with random values
random_array = np.random.random((2,2))
print(f"\nAn array consisting of random values: {random_array}")

#Sometimes, we may want to construct an array from existing arrays by “stacking”
#the existing arrays, either vertically or horizontally. We can use vstack() (or
#row_stack) and hstack() (or column_stack), respectively.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"\nVertical stack{np.vstack((a,b))}")
a = np.array([[7], [8], [9]])
b = np.array([[4], [5], [6]])
print(f"\nHorizontal stack: {np.hstack((a,b))}")

#Array indexing:
#We can index and slice numpy arrays in all the ways we can slice Python lists:
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
b = a[:2, 1:3] #a[row_slice, column_slice]
#:2 → Take rows 0 and 1 (i.e., the first 2 rows; stop before row 2).
#1:3 → Take columns 1 and 2 (i.e., the second and third columns).
#From row 0: columns 1 and 2 → [2, 3]
#From row 1: columns 1 and 2 → [6, 7]
print(f"\nSliced array: {b}")

'''
When working with numpy arrays, it’s often helpful to get the indices (not only the
values) of array elements that meet certain conditions. There are a few numpy
functions:
-argmax (get index of maximum element in array)
-argmin (get index of minimum element in array)
-argsort (get sorted list of indices, by element value, in ascending order)
-where (get indices of elements that meet some condition) 
'''

# Get the mean, max, and sum of an array
print(f"Mean of the array: {numpy_array.mean()}")
print(f"Max of the array: {numpy_array.max()}")
print(f"Sum of the array: {numpy_array.sum()}")

# --- Data Types in NumPy ---
# Every NumPy array is a grid of elements of the same type.
# NumPy provides a large set of numeric datatypes that you can use to construct arrays.
# NumPy tries to guess a datatype when you create an array, but you can also explicitly specify it.

x = np.array([1, 2])  # Let NumPy choose the datatype
y = np.array([1.0, 2.0])  # Let NumPy choose the datatype
z = np.array([1, 2], dtype=np.int64)  # Force a particular datatype
print(x.dtype, y.dtype, z.dtype)  # Expected: int64 float64 int64

# --- Array Math ---
# NumPy comes with many vectorized math functions for computation over elements of an array.
# These functions are highly optimized and are much faster than using Python loops.

# Example: elementwise operations
x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)

# Elementwise sum
print(f"Addition:{x + y}")
print(f"Another way to add:{np.add(x, y)}")

# Elementwise difference
print(f"Subtraction{x - y}")
print(f"Another way to subtract:{np.subtract(x, y)}")

# Elementwise multiplication
print(f"Multiplication{x * y}")
print(f"Another way to multiply:{np.multiply(x, y)}")

# Elementwise division
print(f"Divide{x / y}")
print(f"Another way to divide:{np.divide(x, y)}")

# Elementwise square root
print(f"Square root function:{np.sqrt(x)}")

# --- Aggregate Functions ---
x = np.array([[1, 2], [3, 4], [5, 6]])
print("Max: ",np.max(x))  # Max of all elements
print("Min: ",np.min(x))  # Min of all elements
print("Sum: ",np.sum(x))  # Sum of all elements

# Aggregating across axes
x = np.array([[1, 2], [5, 3], [4, 6]])
print("Max across Axis 0: ",np.max(x, axis=0))  # Max of each column
print("Max across Axis 1: ",np.max(x, axis=1))  # Max of each row

# --- Reshaping and Transposing ---
x = np.array([[1, 2], [3, 4], [5, 6]])
print(x)
print("transpose\n", x.T)

# Transpose 1D row vector to column vector
v = np.array([[1, 2, 3]])
print(v)
print("transpose\n", v.T)

# Column vector
w = np.array([[1], [2], [3]])
print(w)
print(w.shape)

# Flatten to 1D
y = w.reshape(-1,)
print(y)
print(y.shape)

# Reshape from 1D to 2D
y = y.reshape((-1, 1))
print(y)