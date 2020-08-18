import ctypes
# import numpy
import glob

# find the shared library, the path depends on the platform and Python version
libfile = glob.glob('build/*/mysum*.so')[0]

# 1. open the shared library
mylib = ctypes.CDLL(libfile)

# # 2. tell Python the argument and result types of function mysum
# mylib.mysum.restype = ctypes.c_longlong
# mylib.mysum.argtypes = [ctypes.c_int,
#                         numpy.ctypeslib.ndpointer(dtype=numpy.int32)]

# 2. tell Python the argument and result types of function add
mylib.add.restype = ctypes.c_int
mylib.add.argtypes = [ctypes.c_int,
                        ctypes.c_int]

# array = numpy.arange(0, 100000000, 1, numpy.int32)

# print('sum of array: {}'.format(mylib.mysum(len(array), array)))
print('3 * 5: {}'.format(mylib.add(3, 5)))
