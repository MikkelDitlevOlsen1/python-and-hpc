import numpy as np
dir= '/dtu/projects/02613_2025/data/modified_swiss_dwellings/'
file_name='10000_domain.npy'
file_path=dir+file_name
data = np.load(file_path)
print(data.shape)
print(data)