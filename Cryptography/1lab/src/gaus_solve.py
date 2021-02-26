# ctypes_test.py
import ctypes
import pathlib
import numpy as np
from cfiles.numpyctypes import c_ndarray


# Load the shared library into ctypes
libname = pathlib.Path().absolute() / "gaus_solve.so"
c_lib = ctypes.CDLL(libname)

def gaus_solve(input_matrix):
    ret = np.empty(input_matrix.shape, dtype=int)
    N = c_lib.test(c_ndarray(input_matrix, dtype = int, ndim = 2), c_ndarray(ret, dtype = int, ndim = 2))
    return ret[:,:N]

pyarr = [[1,6], [0,2], [4,0], [14,2]]
arr = np.array(pyarr, dtype=int)

print(gaus_solve(arr))