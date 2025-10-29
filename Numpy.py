import numpy as np
print(np.__version__)

arr = np.array([[-1,2,0,4],
                [4,-0.5,6,0],
                [2.6,0,7,8],
                [3,-7,4,2.0]])

# print("No of Dimension..." , arr.ndim)
# print("Shape of array..." , arr.shape)

# print(arr*2)

# print(arr.T)

print("Max element in the array" , arr.max())
print("Max element in the array col-wise" , arr.max(axis=0))
print("Max element in the array row-wise" , arr.max(axis=1))
np.sort(arr,axis=1)
print("sort element in the array" ,arr)