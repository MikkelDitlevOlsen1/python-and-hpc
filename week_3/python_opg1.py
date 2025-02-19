import numpy as np
import time

SIZE = 100

mat = np.random.rand(SIZE, SIZE)
t1= time.time()
double_column = 2 * mat[:, 0]
t1= time.time()-t1

t2= time.time()
double_row = 2 * mat[0, :]
t1= time.time()-t2