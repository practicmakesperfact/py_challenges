import numpy as np

# 2 dimensional array
# arr = np.array([[1,2,3],[2,3,4]]) 

#3 dimensional
# arr = np.array([1,2,3,4],ndmin=5)

#accessing 1-D elements of array
# arr = np.array([1,2,3,4])

# print(arr[2] + arr[3])

# arr = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])

# print(arr)


# print(arr[0,1]) # accessing 2nd element of 1st row

# print(arr[1,1]) # accessing 2nd element of 2nd row
# print(arr[1,1,2]) # accessing 3rd element of 2nd row of 2nd array

# print('number of dimensions:',arr.ndim)
# print(arr.ndim) # dimension
# print(arr.shape) # shape
# print(arr.size) # total elements
# print(arr.dtype) # data type
# print(type(arr))


# slicing
# arr = np.array([[1,2,3,4],[5,6,7,8]])

# print(arr[0:2,2])

# arr = np.array([1,2,3,4,5,6,7,8])

# x = arr.copy() # copy of array
# x[0] = 10
# print(arr) # original array remains unchanged   
# print(x) # copy of array is changed

# print('-------------------')
# y=arr.view() # view of array
# y[0] = 10
# print(y) # view of array is changed
# print(arr) # original array is also changed because view shares the same data


#shape 
 
# arr = np.array([[1,2,3,4],[5,6,7,8]])

# print(arr.shape) 
#Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:

# arr = np.array([1,2,3,4], ndmin=5)
# print(arr)
# print('Shape:', arr.shape)
# print('Last dimension size:', arr.shape[-1])

# Reshape
# 1D array to 2D array
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

new_arr =arr.reshape(4,3) # reshape to 4 rows and 3 columns
print(new_arr)

print('-------------------')
#1d to 3d array
new_ar = arr.reshape(2,3,2) # reshape to 2 arrays of 3 rows and 2 columns
print(new_ar)