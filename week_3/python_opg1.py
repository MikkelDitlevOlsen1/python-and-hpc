import numpy as np
import time

SIZE = 100

reps = range(1000)
mat = np.random.rand(SIZE, SIZE)

t1= time.time()
for i in reps:
    double_column = 2 * mat[:, 0]
t1= time.time()-t1
print(f'time t2= {t1}̈́')

t2= time.time()
for i in reps:
    double_row = 2 * mat[0, :]
t2= time.time()-t2
print(f'time t2= {t2}̈́')