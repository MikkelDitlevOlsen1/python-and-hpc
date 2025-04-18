import multiprocessing
import numpy as np
import matplotlib.pyplot as plt
import time
from multiprocessing.pool import Pool

def mandelbrot_escape_time(c):
    z = 0
    for i in range(100):
        z = z**2 + c
        if np.abs(z) > 2.0:
            return i
    return 100

def generate_mandelbrot_set(points, num_processes):
    chunk_size =len(points)//num_processes
    #chunk_size = 1000
    with Pool(num_processes) as pool:
        fu=pool.map(mandelbrot_escape_time, points, chunksize=chunk_size)
    escape_times = np.array(fu)

    return escape_times

def plot_mandelbrot(escape_times):
    plt.imshow(escape_times, cmap='hot', extent=(-2, 2, -2, 2))
    plt.axis('off')
    plt.savefig('mandelbrot.png', bbox_inches='tight', pad_inches=0)

if __name__ == "__main__":
    width = 800
    height = 800
    xmin, xmax = -2, 2
    ymin, ymax = -2, 2
    num_proclist = [1,2,4,8,16]

    # Precompute points
    x_values = np.linspace(xmin, xmax, width)
    y_values = np.linspace(ymin, ymax, height)
    points = np.array([complex(x, y) for x in x_values for y in y_values])

    # Compute set
    time_list=[None]*len(num_proclist)
    for i,num_proc in enumerate(num_proclist):
        st=time.time()
        mandelbrot_set = generate_mandelbrot_set(points, num_proc)
        runtime=time.time()-st
        time_list[i]=1 if i == 0 else time_list[0]/runtime

    plt.plot(num_proclist, time_list)
    plt.xlabel('Number of Processes')
    plt.ylabel('Speedup')
    plt.title('Mandelbrot Set Generation Time vs Number of Processes')
    plt.savefig('speed1.png')

    # Save set as image
    #mandelbrot_set = mandelbrot_set.reshape((height, width))
    #plot_mandelbrot(mandelbrot_set)