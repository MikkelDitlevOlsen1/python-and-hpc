there are two difrent wayes of useing more cores 
1. multy prosesing (more overhead more time to start up but can be used for more purpeses)

```python
import numpy as np
from multiprocessing.pool import ThreadPool

arr = [0] * 10_000_000
arr_x10 = [arr] * 10
def manual_sum(arr):
    s = 0
    for a in arr:
        s += a
    return s

with ThreadPool(2) as pool:
    pool.map(manual_sum, arr_x10)
```
you can chunk so we dont have as muche overhead 

2. multy trheding used only when you can realese the GIL numpy does this (this is less overhead (faster to start up) and have shared memory but does not work wht generle code)
```python 
import numpy as np
from multiprocessing.pool import ThreadPool
arr = np.zeros((1024, 1024, 1024))
arr_x10 = [arr, arr, arr, arr, arr, 
            arr, arr, arr, arr, arr]
with ThreadPool(4) as pool:
    pool.map(np.sum, arr_x10)
```

speed up time is calculated py s(t)=T(1)/T(n) where n is number of cores used T(n) is the wall time (time it take to run the code for n cores)


### difrent type of parallel
Embarrasingly parallel (perfect senarye 4 cores 4x speeed op)
reality there are a lot of overhead

amdahl's law (speed up wil slow down)
s(p)=T(1)/T(p)=1/((1-f)+f/p)