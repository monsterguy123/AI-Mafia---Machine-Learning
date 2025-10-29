import numpy as np

# arr = np.array([])
# memory = arr.size
# print(memory)

# vec = np.zeros(10)
# vec[4] = 1
# print(vec)

# seq = np.arange(10,50)
# print(seq)

# reverse a vector
# vec = np.arange(10)
# reversed_vec = np.flip(vec)
# print(reversed_vec)

# matrix 3x3 range(0,8)
# arr = np.array([[0,1,2],[2,3,4],[5,6,7]])
# print(arr)

#### 10. Find indices of non-zero elements from \[1,2,0,0,4,0\]

# arr = np.array([1,2,0,0,4,0])

# for index, value in enumerate(arr):
#     if value != 0:
#         print(index,end=" ")
# print("\n")
# print(arr.nonzero()[0])

#### 11. Create a 3x3 identity matrix
# arr = np.eye(3)
# print(arr)

#### 12. Create a 3x3x3 array with random values

# arr = np.random.randn(3,3,3)
# print(arr)
# vec = np.random.randint(0,9,size=(3,3,3))
# print(vec)

#### 13. Create a 10x10 array with random values and find the minimum and maximum values
# arr = np.random.randn(4,4)
# print(arr)
# maximum = np.max(arr)
# minimum = np.min(arr)
# print(maximum,minimum)

#### 14. Create a random vector of size 30 and find the mean value
# arr = np.random.randn(30)
# print(arr.mean())

#### 15. Create a 2d array with 1 on the border and 0 inside
# arr = np.zeros((5, 5), dtype=int)

# arr[0,:] = 1       
# arr[-1, :] = 1      
# arr[:, 0] = 1       
# arr[:, -1] = 1      

# print(arr)

# print(0 * np.nan)
# print(np.nan == np.nan)
# print(np.inf > np.nan)
# print(np.nan - np.nan)
# print(np.nan in set([np.nan]))
# print(0.3 == 3 * 0.1)

## 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal

# arr = np.diag([1, 2, 3, 4], k=-1)
# print(arr)


## 19. Create a 8x8 matrix and fill it with a checkerboard pattern
arr = np.zeros((8, 8), dtype=int)

# for i in range(8):
#     for j in range(8):
#         if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
#             arr[i, j] = 1

arr[1::2, ::2] = 1
arr[::2, 1::2] = 1

print(arr)