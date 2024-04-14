import os
import numpy as np
import scipy.io
mat_directory = 'matdata/'
numpy_directory = 'numpydata/'
if not os.path.exists(numpy_directory):
    os.makedirs(numpy_directory)
slice_size = 81920
for filename in os.listdir(mat_directory):
    if filename.endswith('.mat'):
        data = scipy.io.loadmat(os.path.join(mat_directory, filename))
        original_array = data['IQ_samples'].flatten()
        slices = [original_array[i:i+slice_size] for i in range(0, len(original_array), slice_size)]
        numpy_arrays = [np.array(slice) for slice in slices]
        for i, array in enumerate(numpy_arrays):
            npy_filename = f'{os.path.splitext(filename)[0]}_slice{i+1}-N.npy'
            npy_file_path = os.path.join(numpy_directory, npy_filename)
            np.save(npy_file_path, array)
            print(f"Saved {npy_filename} in {numpy_directory}")
