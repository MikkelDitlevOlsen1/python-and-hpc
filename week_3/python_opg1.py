import numpy as np
import time
import matplotlib.pyplot as plt

sizes = np.logspace(1, 4.5, num=30, dtype=int)
t1_times=[0]*len(sizes)
print(t1_times)
t2_times=[0]*len(sizes)

for n,SIZE in enumerate(sizes):
    reps = range(1000)
    mat = np.random.rand(SIZE, SIZE)


    t1 = time.time()
    for i in reps:
        double_column = 2 * mat[:, 0]
    t1 = time.time() - t1
    t1_times[n]=t1/len(reps)
    print(f'SIZE={SIZE}, time t1= {t1}')

    t2 = time.time()
    for i in reps:
        double_row = 2 * mat[0, :]
    t2 = time.time() - t2
    t2_times[n]=t2/len(reps)
    print(f'SIZE={SIZE}, time t2= {t2}')


sizes_kb = sizes**2 * 8 / 1024  # size of the matrix in kilobytes
mflops_t1 = [2 * SIZE * 1000 / t1 for SIZE, t1 in zip(sizes, t1_times)]
mflops_t2 = [2 * SIZE * 1000 / t2 for SIZE, t2 in zip(sizes, t2_times)]

plt.loglog(sizes_kb, mflops_t1, label='Column Doubling')
plt.loglog(sizes_kb, mflops_t2, label='Row Doubling')
plt.xlabel('Matrix size (KB)')
plt.ylabel('Performance (MFLOP/s)')
plt.legend()
#plt.show()

plt.savefig('plot1_4.png')