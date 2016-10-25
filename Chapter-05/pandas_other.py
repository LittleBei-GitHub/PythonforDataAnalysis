# coding=utf-8

from pandas import DataFrame, Series
import pandas as pd
import numpy as np

if __name__ == '__main__':
    ## 整数索引
    ser = Series(np.arange(3))
    print(ser)
    print(ser[:2])
    print(ser.ix[:1]) # ix进行切片是包含的

    ser3 = Series(range(3), index=[-5, 1, 3])
    print(ser3)
    print(ser3.iget_value(1))

    frame = DataFrame(np.arange(6).reshape(3, 2), index=[2, 0, 1])
    print(frame)
    print(frame.irow(0))

    ## 面板数据