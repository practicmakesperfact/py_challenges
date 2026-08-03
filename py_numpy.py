import numpy as np

# 2 dimensional array
# arr = np.array([[1,2,3],[2,3,4]]) 

#3 dimensional
# arr = np.array([1,2,3,4],ndmin=5)

#accessing 1-D elements of array
# arr = np.array([1,2,3,4])

# print(arr[2] + arr[3])

arr = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])

print(arr)

# print(arr[0,1]) # accessing 2nd element of 1st row

# print(arr[1,1]) # accessing 2nd element of 2nd row
print(arr[1,1,2]) # accessing 3rd element of 2nd row of 2nd array

# print('number of dimensions:',arr.ndim)
# print(arr.ndim) # dimension
# print(arr.shape) # shape
# print(arr.size) # total elements
# print(arr.dtype) # data type
# print(type(arr))
