import numpy as np

# 2 dimensional array
# arr = np.array([[1,2,3],[2,3,4]]) 

#3 dimensional
arr = np.array([1,2,3,4],ndmin=5)


print(arr)
print('number of dimensions:',arr.ndim)
# print(arr.ndim) # dimension
# print(arr.shape) # shape
# print(arr.size) # total elements
# print(arr.dtype) # data type
# print(type(arr))
