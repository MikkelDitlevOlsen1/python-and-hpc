import numpy as np
#1.1

def standardize_rows(matrix, mean, std):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = (matrix[i][j] - mean[j]) / std[j]

    return matrix

#a=standardize_rows([[1,2,3],[4,5,6]], [0.5,1,3], [1,2,3])
#print(a)

#1.2
def outer(a,b):
    outer = []
    for i in range(len(a)):
        row = []
        for j in range(len(b)):
            row.append(a[i] * b[j])
        outer.append(row)
    return np.array(outer)

def outer_np(a,b):
    return [a[:,None]*b]
   
#a=outer([1,2],[3,4,5]) 
#print(a)

    
    
#1.3
def distmat_1d(a,b):
    c=np.abs(a[:,None]-b[None])
    return c

#a=distmat_1d(np.array([1,2]),np.array([3,0.5,1]))
#print(a)

print(np.array([[1,2,4],[2,3,4]]).shape)
