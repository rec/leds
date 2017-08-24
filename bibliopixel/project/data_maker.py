import ctypes, os
from multiprocessing.sharedctypes import RawArray
from .. util import log

try:
    import numpy
except:
    numpy = None

NUMPY_DTYPE = os.environ.get('BP_NUMPY_DTYPE')


def Maker(floating=None, shared_memory=False, numpy_dtype=NUMPY_DTYPE):
    def list_maker(size):
        return [(0, 0, 0)] * size

    if numpy_dtype:
        if numpy:
            log.info('Using numpy')
        else:
            log.error('numpy module is not available.')
            numpy_dtype = None

    if not (shared_memory or numpy_dtype):
        return bytearray, list_maker

    byte_type, float_type = ctypes.c_uint8, ctypes.c_float
    floating = (not shared_memory) if (floating is None) else floating
    number_type = float_type if floating else byte_type

    if shared_memory:
        def shared_list_maker(type):
            # Note https://stackoverflow.com/questions/37705974/
            return lambda size: RawArray(type, size)

        return shared_list_maker(byte_type), shared_list_maker(3 * number_type)

    def numpy_list_maker(size):
        return numpy.array(list_maker(size), dtype=numpy_dtype)

    return bytearray, numpy_list_maker


MAKER = Maker()
ColorList = MAKER[1]
