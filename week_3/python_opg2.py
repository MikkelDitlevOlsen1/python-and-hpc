import os
import blosc
import numpy as np
import sys
import time


def write_numpy(arr, file_name):
    np.save(f"{file_name}.npy", arr)
    os.sync()

def write_blosc(arr, file_name, cname="lz4"):
    b_arr = blosc.pack_array(arr, cname=cname)
    with open(f"{file_name}.bl", "wb") as w:
        w.write(b_arr)
    os.sync()

def read_numpy(file_name):
    return np.load(f"{file_name}.npy")

def read_blosc(file_name):
    with open(f"{file_name}.bl", "rb") as r:
        b_arr = r.read()
    return blosc.unpack_array(b_arr)

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python python_opg2.py <n>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("The argument must be an integer.")
        sys.exit(1)

    arr = np.zeros((n, n, n), dtype='uint8')
 
    # Timing write_numpy
    start_time = time.time()
    write_numpy(arr, "numpy_array")
    numpy_write_time = time.time() - start_time

    # Timing write_blosc
    start_time = time.time()
    write_blosc(arr, "blosc_array")
    blosc_write_time = time.time() - start_time

    # Timing read_numpy
    start_time = time.time()
    numpy_arr = read_numpy("numpy_array")
    numpy_read_time = time.time() - start_time

    # Timing read_blosc
    start_time = time.time()
    blosc_arr = read_blosc("blosc_array")
    blosc_read_time = time.time() - start_time

    print(numpy_write_time)
    print(blosc_write_time)
    print(numpy_read_time)
    print(blosc_read_time)