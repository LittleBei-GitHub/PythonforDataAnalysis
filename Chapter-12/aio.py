# coding=utf-8

import numpy as np

if __name__ == '__name__':
    ## 内存映像文件
    mmap = np.memmap('mymmap', dtype='float64', mode='w+', shape=(10000, 10000))
    print(mmap)
    section = mmap[:5]
    section[:] = np.random.randn(5, 10000)
    mmap.flush()
    print(mmap)